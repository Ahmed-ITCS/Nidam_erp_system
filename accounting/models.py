from django.db import models
from django.contrib.auth.models import User
from sales.models import Customer, Invoice
from decimal import Decimal

class Account(models.Model):
    ACCOUNT_TYPES = [
        ('asset', 'Asset'),
        ('liability', 'Liability'),
        ('equity', 'Equity'),
        ('revenue', 'Revenue'),
        ('expense', 'Expense'),
    ]

    ACCOUNT_SUBTYPES = [
        ('current_asset', 'Current Asset'),
        ('fixed_asset', 'Fixed Asset'),
        ('current_liability', 'Current Liability'),
        ('long_term_liability', 'Long Term Liability'),
        ('owners_equity', 'Owners Equity'),
        ('sales_revenue', 'Sales Revenue'),
        ('other_revenue', 'Other Revenue'),
        ('cost_of_goods_sold', 'Cost of Goods Sold'),
        ('operating_expense', 'Operating Expense'),
        ('other_expense', 'Other Expense'),
    ]

    account_number = models.CharField(max_length=20, unique=True)
    account_name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    account_subtype = models.CharField(max_length=30, choices=ACCOUNT_SUBTYPES)
    parent_account = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.account_number} - {self.account_name}"

    @property
    def balance(self):
        # Calculate balance from journal entries
        debits = JournalEntry.objects.filter(account=self, entry_type='debit').aggregate(models.Sum('amount'))['amount__sum'] or 0
        credits = JournalEntry.objects.filter(account=self, entry_type='credit').aggregate(models.Sum('amount'))['amount__sum'] or 0
        
        if self.account_type in ['asset', 'expense']:
            return debits - credits
        else:
            return credits - debits

class Vendor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    tax_number = models.CharField(max_length=50, blank=True)
    payment_terms = models.CharField(max_length=50, default='Net 30')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class JournalEntry(models.Model):
    ENTRY_TYPES = [
        ('debit', 'Debit'),
        ('credit', 'Credit'),
    ]

    entry_number = models.CharField(max_length=50, unique=True)
    date = models.DateField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    entry_type = models.CharField(max_length=10, choices=ENTRY_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    reference_number = models.CharField(max_length=50, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.entry_number} - {self.account.account_name} - {self.amount}"

    class Meta:
        ordering = ['-date', '-created_at']

class Bill(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('paid', 'Paid'),
        ('partially_paid', 'Partially Paid'),
        ('overdue', 'Overdue'),
        ('cancelled', 'Cancelled'),
    ]

    bill_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    bill_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Bill {self.bill_number} - {self.vendor.name}"

class BillItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='items')
    description = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    line_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.line_total = self.unit_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.description} - {self.quantity} units"

class Payment(models.Model):
    PAYMENT_TYPES = [
        ('customer_payment', 'Customer Payment'),
        ('vendor_payment', 'Vendor Payment'),
        ('expense_payment', 'Expense Payment'),
        ('other', 'Other'),
    ]

    PAYMENT_METHODS = [
        ('cash', 'Cash'),
        ('check', 'Check'),
        ('bank_transfer', 'Bank Transfer'),
        ('credit_card', 'Credit Card'),
        ('online', 'Online Payment'),
    ]

    payment_number = models.CharField(max_length=50, unique=True)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPES)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    reference_number = models.CharField(max_length=50, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, blank=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True, blank=True)
    bill = models.ForeignKey(Bill, on_delete=models.SET_NULL, null=True, blank=True)
    bank_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment {self.payment_number} - {self.amount}"

class BudgetCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Budget Categories"

class Budget(models.Model):
    name = models.CharField(max_length=100)
    fiscal_year = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    total_budget = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - FY {self.fiscal_year}"

class BudgetItem(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='items')
    category = models.ForeignKey(BudgetCategory, on_delete=models.CASCADE)
    budgeted_amount = models.DecimalField(max_digits=10, decimal_places=2)
    actual_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    variance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.variance = self.actual_amount - self.budgeted_amount
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.budget.name} - {self.category.name}"
