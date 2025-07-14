from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from sales.models import Customer, Product, Quote, SalesOrder, Invoice
from accounting.models import Account, Payment, Bill
from hr.models import Employee, Department, LeaveRequest
from datetime import datetime, timedelta

@login_required
def dashboard(request):
    # Get statistics for dashboard
    today = datetime.now().date()
    last_month = today - timedelta(days=30)
    
    # Sales stats
    total_customers = Customer.objects.count()
    total_products = Product.objects.count()
    pending_quotes = Quote.objects.filter(status='sent').count()
    active_orders = SalesOrder.objects.filter(status__in=['confirmed', 'processing']).count()
    
    # Recent invoices
    recent_invoices = Invoice.objects.filter(created_at__gte=last_month).order_by('-created_at')[:5]
    
    # Monthly sales
    monthly_sales = Invoice.objects.filter(
        invoice_date__gte=last_month,
        status='paid'
    ).aggregate(total=Sum('total_amount'))['total'] or 0
    
    # Employee stats
    total_employees = Employee.objects.filter(employment_status='active').count()
    total_departments = Department.objects.filter(is_active=True).count()
    pending_leave_requests = LeaveRequest.objects.filter(status='pending').count()
    
    # Recent activities (simplified)
    activities = [
        {'action': 'New customer registered', 'time': '2 hours ago'},
        {'action': 'Invoice INV-001 paid', 'time': '4 hours ago'},
        {'action': 'Leave request submitted', 'time': '1 day ago'},
        {'action': 'New product added', 'time': '2 days ago'},
    ]
    
    context = {
        'total_customers': total_customers,
        'total_products': total_products,
        'pending_quotes': pending_quotes,
        'active_orders': active_orders,
        'recent_invoices': recent_invoices,
        'monthly_sales': monthly_sales,
        'total_employees': total_employees,
        'total_departments': total_departments,
        'pending_leave_requests': pending_leave_requests,
        'activities': activities,
    }
    
    return render(request, 'core/dashboard.html', context)

@login_required
def profile(request):
    return render(request, 'core/profile.html')

@login_required
def settings(request):
    return render(request, 'core/settings.html')
