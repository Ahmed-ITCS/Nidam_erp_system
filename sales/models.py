from django.db import models
from django.contrib.auth.models import User
from core.models import Address
from decimal import Decimal

class Customer(models.Model):
    CUSTOMER_TYPES = [
        ('individual', 'Individual'),
        ('business', 'Business'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    customer_type = models.CharField(max_length=20, choices=CUSTOMER_TYPES, default='individual')
    tax_number = models.CharField(max_length=50, blank=True)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    billing_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, related_name='billing_customers')
    shipping_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, related_name='shipping_customers')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    PRODUCT_TYPES = [
        ('product', 'Product'),
        ('service', 'Service'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    sku = models.CharField(max_length=50, unique=True)
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPES, default='product')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity_in_stock = models.IntegerField(default=0)
    minimum_stock_level = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def profit_margin(self):
        if self.unit_price > 0:
            return ((self.unit_price - self.cost_price) / self.unit_price) * 100
        return 0

class Quote(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('expired', 'Expired'),
    ]

    quote_number = models.CharField(max_length=50, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sales_rep = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    quote_date = models.DateField()
    valid_until = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Quote {self.quote_number} - {self.customer.name}"

class QuoteItem(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    line_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        discount_amount = (self.unit_price * self.quantity) * (self.discount / 100)
        self.line_total = (self.unit_price * self.quantity) - discount_amount
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} units"

class SalesOrder(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    order_number = models.CharField(max_length=50, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sales_rep = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    quote = models.ForeignKey(Quote, on_delete=models.SET_NULL, null=True, blank=True)
    order_date = models.DateField()
    expected_delivery_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.order_number} - {self.customer.name}"

class SalesOrderItem(models.Model):
    order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    line_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        discount_amount = (self.unit_price * self.quantity) * (self.discount / 100)
        self.line_total = (self.unit_price * self.quantity) - discount_amount
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} units"

class Invoice(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('paid', 'Paid'),
        ('partially_paid', 'Partially Paid'),
        ('overdue', 'Overdue'),
        ('cancelled', 'Cancelled'),
    ]

    invoice_number = models.CharField(max_length=50, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.SET_NULL, null=True, blank=True)
    invoice_date = models.DateField()
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
        return f"Invoice {self.invoice_number} - {self.customer.name}"

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    line_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        discount_amount = (self.unit_price * self.quantity) * (self.discount / 100)
        self.line_total = (self.unit_price * self.quantity) - discount_amount
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} units"
