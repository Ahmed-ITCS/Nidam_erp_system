from django.contrib import admin
from .models import Company, UserProfile, Address, AuditLog

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'tax_number', 'created_at']
    search_fields = ['name', 'email', 'tax_number']
    list_filter = ['created_at']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'phone', 'created_at']
    search_fields = ['user__first_name', 'user__last_name', 'user__email']
    list_filter = ['role', 'created_at']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['street', 'city', 'state', 'postal_code', 'country', 'address_type']
    search_fields = ['street', 'city', 'state', 'postal_code']
    list_filter = ['address_type', 'country', 'is_default']

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'action', 'model_name', 'object_id', 'timestamp']
    search_fields = ['user__username', 'model_name', 'object_id']
    list_filter = ['action', 'model_name', 'timestamp']
    readonly_fields = ['timestamp']
