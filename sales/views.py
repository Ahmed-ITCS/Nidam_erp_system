from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Customer, Product, Quote, SalesOrder, Invoice

@login_required
def sales_dashboard(request):
    context = {
        'total_customers': Customer.objects.count(),
        'total_products': Product.objects.count(),
        'pending_quotes': Quote.objects.filter(status='sent').count(),
        'active_orders': SalesOrder.objects.filter(status__in=['confirmed', 'processing']).count(),
    }
    return render(request, 'sales/dashboard.html', context)

@login_required
def customer_list(request):
    customers = Customer.objects.all().order_by('-created_at')
    return render(request, 'sales/customer_list.html', {'customers': customers})

@login_required
def customer_add(request):
    if request.method == 'POST':
        # Handle form submission
        messages.success(request, 'Customer added successfully!')
        return redirect('sales:customer_list')
    return render(request, 'sales/customer_form.html')

@login_required
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'sales/customer_detail.html', {'customer': customer})

@login_required
def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'sales/product_list.html', {'products': products})

@login_required
def product_add(request):
    if request.method == 'POST':
        # Handle form submission
        messages.success(request, 'Product added successfully!')
        return redirect('sales:product_list')
    return render(request, 'sales/product_form.html')

@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'sales/product_detail.html', {'product': product})

@login_required
def quote_list(request):
    quotes = Quote.objects.all().order_by('-created_at')
    return render(request, 'sales/quote_list.html', {'quotes': quotes})

@login_required
def quote_add(request):
    if request.method == 'POST':
        # Handle form submission
        messages.success(request, 'Quote created successfully!')
        return redirect('sales:quote_list')
    return render(request, 'sales/quote_form.html')

@login_required
def quote_detail(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    return render(request, 'sales/quote_detail.html', {'quote': quote})

@login_required
def order_list(request):
    orders = SalesOrder.objects.all().order_by('-created_at')
    return render(request, 'sales/order_list.html', {'orders': orders})

@login_required
def order_add(request):
    if request.method == 'POST':
        # Handle form submission
        messages.success(request, 'Order created successfully!')
        return redirect('sales:order_list')
    return render(request, 'sales/order_form.html')

@login_required
def order_detail(request, pk):
    order = get_object_or_404(SalesOrder, pk=pk)
    return render(request, 'sales/order_detail.html', {'order': order})

@login_required
def invoice_list(request):
    invoices = Invoice.objects.all().order_by('-created_at')
    return render(request, 'sales/invoice_list.html', {'invoices': invoices})

@login_required
def invoice_add(request):
    if request.method == 'POST':
        # Handle form submission
        messages.success(request, 'Invoice created successfully!')
        return redirect('sales:invoice_list')
    return render(request, 'sales/invoice_form.html')

@login_required
def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'sales/invoice_detail.html', {'invoice': invoice})
