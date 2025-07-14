from django.contrib import admin
from .models import Account, Vendor, JournalEntry, Bill, BillItem, Payment, BudgetCategory, Budget, BudgetItem

class BillItemInline(admin.TabularInline):
    model = BillItem
    extra = 1

class BudgetItemInline(admin.TabularInline):
    model = BudgetItem
    extra = 1

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['account_number', 'account_name', 'account_type', 'account_subtype', 'balance', 'is_active']
    search_fields = ['account_number', 'account_name']
    list_filter = ['account_type', 'account_subtype', 'is_active', 'created_at']

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'payment_terms', 'is_active']
    search_fields = ['name', 'email', 'phone']
    list_filter = ['is_active', 'created_at']

@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ['entry_number', 'date', 'account', 'description', 'entry_type', 'amount']
    search_fields = ['entry_number', 'description', 'account__account_name']
    list_filter = ['entry_type', 'date', 'created_at']

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['bill_number', 'vendor', 'bill_date', 'due_date', 'status', 'total_amount', 'balance']
    search_fields = ['bill_number', 'vendor__name']
    list_filter = ['status', 'bill_date', 'due_date', 'created_at']
    inlines = [BillItemInline]

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['payment_number', 'payment_type', 'payment_date', 'amount', 'payment_method']
    search_fields = ['payment_number', 'reference_number']
    list_filter = ['payment_type', 'payment_method', 'payment_date', 'created_at']

@admin.register(BudgetCategory)
class BudgetCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'account', 'is_active']
    search_fields = ['name', 'account__account_name']
    list_filter = ['is_active', 'created_at']

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ['name', 'fiscal_year', 'start_date', 'end_date', 'total_budget', 'is_active']
    search_fields = ['name']
    list_filter = ['fiscal_year', 'is_active', 'created_at']
    inlines = [BudgetItemInline]
