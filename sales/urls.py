from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    path('', views.sales_dashboard, name='dashboard'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.customer_add, name='customer_add'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_add, name='product_add'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('quotes/', views.quote_list, name='quote_list'),
    path('quotes/add/', views.quote_add, name='quote_add'),
    path('quotes/<int:pk>/', views.quote_detail, name='quote_detail'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/add/', views.order_add, name='order_add'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/add/', views.invoice_add, name='invoice_add'),
    path('invoices/<int:pk>/', views.invoice_detail, name='invoice_detail'),
]
