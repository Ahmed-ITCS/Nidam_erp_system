from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Employee, Department, Attendance, LeaveRequest, Payroll, PerformanceReview, Training

@login_required
def hr_dashboard(request):
    context = {
        'total_employees': Employee.objects.filter(employment_status='active').count(),
        'total_departments': Department.objects.filter(is_active=True).count(),
        'pending_leave_requests': LeaveRequest.objects.filter(status='pending').count(),
        'active_training': Training.objects.filter(is_active=True).count(),
    }
    return render(request, 'hr/dashboard.html', context)

@login_required
def employee_list(request):
    employees = Employee.objects.all().order_by('-created_at')
    return render(request, 'hr/employee_list.html', {'employees': employees})

@login_required
def employee_add(request):
    if request.method == 'POST':
        messages.success(request, 'Employee added successfully!')
        return redirect('hr:employee_list')
    return render(request, 'hr/employee_form.html')

@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'hr/employee_detail.html', {'employee': employee})

@login_required
def department_list(request):
    departments = Department.objects.all().order_by('-created_at')
    return render(request, 'hr/department_list.html', {'departments': departments})

@login_required
def department_add(request):
    if request.method == 'POST':
        messages.success(request, 'Department added successfully!')
        return redirect('hr:department_list')
    return render(request, 'hr/department_form.html')

@login_required
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'hr/department_detail.html', {'department': department})

@login_required
def attendance_list(request):
    attendance = Attendance.objects.all().order_by('-date')
    return render(request, 'hr/attendance_list.html', {'attendance': attendance})

@login_required
def attendance_add(request):
    if request.method == 'POST':
        messages.success(request, 'Attendance record added successfully!')
        return redirect('hr:attendance_list')
    return render(request, 'hr/attendance_form.html')

@login_required
def leave_request_list(request):
    leave_requests = LeaveRequest.objects.all().order_by('-created_at')
    return render(request, 'hr/leave_request_list.html', {'leave_requests': leave_requests})

@login_required
def leave_request_add(request):
    if request.method == 'POST':
        messages.success(request, 'Leave request submitted successfully!')
        return redirect('hr:leave_request_list')
    return render(request, 'hr/leave_request_form.html')

@login_required
def leave_request_detail(request, pk):
    leave_request = get_object_or_404(LeaveRequest, pk=pk)
    return render(request, 'hr/leave_request_detail.html', {'leave_request': leave_request})

@login_required
def payroll_list(request):
    payrolls = Payroll.objects.all().order_by('-created_at')
    return render(request, 'hr/payroll_list.html', {'payrolls': payrolls})

@login_required
def payroll_add(request):
    if request.method == 'POST':
        messages.success(request, 'Payroll processed successfully!')
        return redirect('hr:payroll_list')
    return render(request, 'hr/payroll_form.html')

@login_required
def payroll_detail(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    return render(request, 'hr/payroll_detail.html', {'payroll': payroll})

@login_required
def performance_review_list(request):
    reviews = PerformanceReview.objects.all().order_by('-created_at')
    return render(request, 'hr/performance_review_list.html', {'reviews': reviews})

@login_required
def performance_review_add(request):
    if request.method == 'POST':
        messages.success(request, 'Performance review added successfully!')
        return redirect('hr:performance_review_list')
    return render(request, 'hr/performance_review_form.html')

@login_required
def performance_review_detail(request, pk):
    review = get_object_or_404(PerformanceReview, pk=pk)
    return render(request, 'hr/performance_review_detail.html', {'review': review})

@login_required
def training_list(request):
    training_sessions = Training.objects.all().order_by('-created_at')
    return render(request, 'hr/training_list.html', {'training_sessions': training_sessions})

@login_required
def training_add(request):
    if request.method == 'POST':
        messages.success(request, 'Training session added successfully!')
        return redirect('hr:training_list')
    return render(request, 'hr/training_form.html')

@login_required
def training_detail(request, pk):
    training = get_object_or_404(Training, pk=pk)
    return render(request, 'hr/training_detail.html', {'training': training})
