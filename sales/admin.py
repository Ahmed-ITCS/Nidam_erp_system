from django.contrib import admin
from .models import Customer, Product, Quote, QuoteItem, SalesOrder, SalesOrderItem, Invoice, InvoiceItem

class QuoteItemInline(admin.TabularInline):
    model = QuoteItem
    extra = 1

class SalesOrderItemInline(admin.TabularInline):
    model = SalesOrderItem
    extra = 1

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'customer_type', 'credit_limit', 'is_active']
    search_fields = ['name', 'email', 'phone']
    list_filter = ['customer_type', 'is_active', 'created_at']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'sku', 'product_type', 'unit_price', 'cost_price', 'quantity_in_stock', 'is_active']
    search_fields = ['name', 'sku', 'description']
    list_filter = ['product_type', 'is_active', 'created_at']

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['quote_number', 'customer', 'sales_rep', 'quote_date', 'status', 'total_amount']
    search_fields = ['quote_number', 'customer__name']
    list_filter = ['status', 'quote_date', 'created_at']
    inlines = [QuoteItemInline]

@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'customer', 'sales_rep', 'order_date', 'status', 'total_amount']
    search_fields = ['order_number', 'customer__name']
    list_filter = ['status', 'order_date', 'created_at']
    inlines = [SalesOrderItemInline]

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'customer', 'invoice_date', 'due_date', 'status', 'total_amount', 'balance']
    search_fields = ['invoice_number', 'customer__name']
    list_filter = ['status', 'invoice_date', 'due_date', 'created_at']
    inlines = [InvoiceItemInline]
