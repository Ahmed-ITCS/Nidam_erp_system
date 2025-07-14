from django.urls import path
from . import views

app_name = 'accounting'

urlpatterns = [
    path('', views.accounting_dashboard, name='dashboard'),
    path('accounts/', views.account_list, name='account_list'),
    path('accounts/add/', views.account_add, name='account_add'),
    path('accounts/<int:pk>/', views.account_detail, name='account_detail'),
    path('vendors/', views.vendor_list, name='vendor_list'),
    path('vendors/add/', views.vendor_add, name='vendor_add'),
    path('vendors/<int:pk>/', views.vendor_detail, name='vendor_detail'),
    path('journal/', views.journal_entry_list, name='journal_entry_list'),
    path('journal/add/', views.journal_entry_add, name='journal_entry_add'),
    path('bills/', views.bill_list, name='bill_list'),
    path('bills/add/', views.bill_add, name='bill_add'),
    path('bills/<int:pk>/', views.bill_detail, name='bill_detail'),
    path('payments/', views.payment_list, name='payment_list'),
    path('payments/add/', views.payment_add, name='payment_add'),
    path('payments/<int:pk>/', views.payment_detail, name='payment_detail'),
    path('budgets/', views.budget_list, name='budget_list'),
    path('budgets/add/', views.budget_add, name='budget_add'),
    path('budgets/<int:pk>/', views.budget_detail, name='budget_detail'),
    path('reports/', views.reports, name='reports'),
    path('reports/budget-variance/', views.budget_variance_report, name='budget_variance_report'),
    path('reports/vendor-summary/', views.vendor_summary_report, name='vendor_summary_report'),
    path('reports/tax-summary/', views.tax_summary_report, name='tax_summary_report'),
    path('reports/balance-sheet/', views.balance_sheet_report, name='balance_sheet_report'),
    path('reports/profit-loss/', views.profit_loss_report, name='profit_loss_report'),
    path('reports/cash-flow/', views.cash_flow_report, name='cash_flow_report'),
]
