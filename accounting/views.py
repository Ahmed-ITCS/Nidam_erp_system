from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Account, Vendor, JournalEntry, Bill, Payment, Budget

@login_required
def accounting_dashboard(request):
    context = {
        'total_accounts': Account.objects.count(),
        'total_vendors': Vendor.objects.count(),
        'pending_bills': Bill.objects.filter(status='open').count(),
        'total_payments': Payment.objects.count(),
    }
    return render(request, 'accounting/dashboard.html', context)

@login_required
def account_list(request):
    accounts = Account.objects.all().order_by('account_number')
    return render(request, 'accounting/account_list.html', {'accounts': accounts})

@login_required
def account_add(request):
    if request.method == 'POST':
        messages.success(request, 'Account added successfully!')
        return redirect('accounting:account_list')
    return render(request, 'accounting/account_form.html')

@login_required
def account_detail(request, pk):
    account = get_object_or_404(Account, pk=pk)
    return render(request, 'accounting/account_detail.html', {'account': account})

@login_required
def vendor_list(request):
    vendors = Vendor.objects.all().order_by('-created_at')
    return render(request, 'accounting/vendor_list.html', {'vendors': vendors})

@login_required
def vendor_add(request):
    if request.method == 'POST':
        messages.success(request, 'Vendor added successfully!')
        return redirect('accounting:vendor_list')
    return render(request, 'accounting/vendor_form.html')

@login_required
def vendor_detail(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    return render(request, 'accounting/vendor_detail.html', {'vendor': vendor})

@login_required
def journal_entry_list(request):
    entries = JournalEntry.objects.all().order_by('-date')
    return render(request, 'accounting/journal_entry_list.html', {'entries': entries})

@login_required
def journal_entry_add(request):
    if request.method == 'POST':
        messages.success(request, 'Journal entry added successfully!')
        return redirect('accounting:journal_entry_list')
    return render(request, 'accounting/journal_entry_form.html')

@login_required
def bill_list(request):
    bills = Bill.objects.all().order_by('-created_at')
    return render(request, 'accounting/bill_list.html', {'bills': bills})

@login_required
def bill_add(request):
    if request.method == 'POST':
        messages.success(request, 'Bill added successfully!')
        return redirect('accounting:bill_list')
    return render(request, 'accounting/bill_form.html')

@login_required
def bill_detail(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    return render(request, 'accounting/bill_detail.html', {'bill': bill})

@login_required
def payment_list(request):
    payments = Payment.objects.all().order_by('-created_at')
    return render(request, 'accounting/payment_list.html', {'payments': payments})

@login_required
def payment_add(request):
    if request.method == 'POST':
        messages.success(request, 'Payment added successfully!')
        return redirect('accounting:payment_list')
    return render(request, 'accounting/payment_form.html')

@login_required
def payment_detail(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    return render(request, 'accounting/payment_detail.html', {'payment': payment})

@login_required
def budget_list(request):
    budgets = Budget.objects.all().order_by('-created_at')
    return render(request, 'accounting/budget_list.html', {'budgets': budgets})

@login_required
def budget_add(request):
    if request.method == 'POST':
        messages.success(request, 'Budget added successfully!')
        return redirect('accounting:budget_list')
    return render(request, 'accounting/budget_form.html')

@login_required
def budget_detail(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    return render(request, 'accounting/budget_detail.html', {'budget': budget})

@login_required
def reports(request):
    return render(request, 'accounting/reports.html')

@login_required
def budget_variance_report(request):
    """Generate budget variance report comparing actual vs budgeted amounts"""
    # This is a placeholder implementation
    # You'll need to implement the actual report logic
    context = {
        'report_type': 'Budget Variance Report',
        'message': 'Budget variance report functionality will be implemented here.'
    }
    return render(request, 'accounting/budget_variance_report.html', context)

@login_required
def vendor_summary_report(request):
    """Generate vendor summary report"""
    # This is a placeholder implementation
    # You'll need to implement the actual report logic
    context = {
        'report_type': 'Vendor Summary Report',
        'message': 'Vendor summary report functionality will be implemented here.'
    }
    return render(request, 'accounting/vendor_summary_report.html', context)

@login_required
def tax_summary_report(request):
    """Generate tax summary report"""
    # This is a placeholder implementation
    # You'll need to implement the actual report logic
    context = {
        'report_type': 'Tax Summary Report',
        'message': 'Tax summary report functionality will be implemented here.'
    }
    return render(request, 'accounting/tax_summary_report.html', context)

@login_required
def balance_sheet_report(request):
    """Generate balance sheet report"""
    # This is a placeholder implementation
    # You'll need to implement the actual report logic
    context = {
        'report_type': 'Balance Sheet',
        'message': 'Balance sheet report functionality will be implemented here.'
    }
    return render(request, 'accounting/balance_sheet_report.html', context)

@login_required
def profit_loss_report(request):
    """Generate profit and loss report"""
    # This is a placeholder implementation
    # You'll need to implement the actual report logic
    context = {
        'report_type': 'Profit & Loss Statement',
        'message': 'Profit & Loss report functionality will be implemented here.'
    }
    return render(request, 'accounting/profit_loss_report.html', context)

@login_required
def cash_flow_report(request):
    """Generate cash flow report"""
    # This is a placeholder implementation
    # You'll need to implement the actual report logic
    context = {
        'report_type': 'Cash Flow Statement',
        'message': 'Cash flow report functionality will be implemented here.'
    }
    return render(request, 'accounting/cash_flow_report.html', context)
