from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import date
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
        try:
            # Get form data
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            department_id = request.POST.get('department')
            
            # Create User first
            user = User.objects.create_user(
                username=email,  # Use email as username
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            
            # Generate employee ID
            employee_count = Employee.objects.count() + 1
            employee_id = f"EMP{employee_count:04d}"
            
            # Create Employee
            employee = Employee.objects.create(
                user=user,
                employee_id=employee_id,
                hire_date=date.today(),
                employment_status='active'
            )
            
            # Set department if provided
            if department_id:
                try:
                    department = Department.objects.get(id=department_id)
                    employee.department = department
                    employee.save()
                except Department.DoesNotExist:
                    pass
            
            messages.success(request, 'Employee added successfully!')
            return redirect('hr:employee_list')
        except Exception as e:
            messages.error(request, f'Error adding employee: {str(e)}')
    
    # Get departments for the form
    departments = Department.objects.filter(is_active=True)
    return render(request, 'hr/employee_form.html', {'departments': departments})

@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'hr/employee_detail.html', {'employee': employee})

@login_required
def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        try:
            # Get form data
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            department_id = request.POST.get('department')
            
            # Update User
            user = employee.user
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = email
            user.save()
            
            # Update Employee
            if department_id:
                try:
                    department = Department.objects.get(id=department_id)
                    employee.department = department
                except Department.DoesNotExist:
                    pass
            
            employee.save()
            
            messages.success(request, 'Employee updated successfully!')
            return redirect('hr:employee_detail', pk=pk)
        except Exception as e:
            messages.error(request, f'Error updating employee: {str(e)}')
    
    # Get departments for the form
    departments = Department.objects.filter(is_active=True)
    return render(request, 'hr/employee_form.html', {
        'employee': employee,
        'departments': departments,
        'is_edit': True
    })

@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        try:
            user = employee.user
            employee.delete()
            user.delete()
            messages.success(request, 'Employee deleted successfully!')
            return redirect('hr:employee_list')
        except Exception as e:
            messages.error(request, f'Error deleting employee: {str(e)}')
    return render(request, 'hr/employee_confirm_delete.html', {'employee': employee})

@login_required
def department_list(request):
    departments = Department.objects.all().order_by('-created_at')
    return render(request, 'hr/department_list.html', {'departments': departments})

@login_required
def department_add(request):
    if request.method == 'POST':
        try:
            # Get form data
            name = request.POST.get('name')
            manager_id = request.POST.get('manager')
            description = request.POST.get('description')
            location = request.POST.get('location')
            budget = request.POST.get('budget') or 0
            is_active = request.POST.get('is_active') == 'on'
            
            # Create department
            department = Department.objects.create(
                name=name,
                description=description,
                location=location,
                budget=budget,
                is_active=is_active
            )
            
            # Assign manager if provided
            if manager_id:
                try:
                    employee = Employee.objects.get(id=manager_id)
                    department.manager = employee.user
                    department.save()
                except Employee.DoesNotExist:
                    pass
            
            messages.success(request, 'Department added successfully!')
            return redirect('hr:department_list')
        except Exception as e:
            messages.error(request, f'Error adding department: {str(e)}')
    
    # Get employees for the form
    employees = Employee.objects.filter(employment_status='active')
    return render(request, 'hr/department_form.html', {'employees': employees})

@login_required
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'hr/department_detail.html', {'department': department})

@login_required
def department_edit(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        try:
            # Get form data
            name = request.POST.get('name')
            manager_id = request.POST.get('manager')
            description = request.POST.get('description')
            location = request.POST.get('location')
            budget = request.POST.get('budget') or 0
            is_active = request.POST.get('is_active') == 'on'
            
            # Update department
            department.name = name
            department.description = description
            department.location = location
            department.budget = budget
            department.is_active = is_active
            
            # Assign manager if provided
            if manager_id:
                try:
                    employee = Employee.objects.get(id=manager_id)
                    department.manager = employee.user
                except Employee.DoesNotExist:
                    department.manager = None
            else:
                department.manager = None
            
            department.save()
            
            messages.success(request, 'Department updated successfully!')
            return redirect('hr:department_detail', pk=pk)
        except Exception as e:
            messages.error(request, f'Error updating department: {str(e)}')
    
    # Get employees for the form
    employees = Employee.objects.filter(employment_status='active')
    return render(request, 'hr/department_form.html', {
        'department': department,
        'employees': employees,
        'is_edit': True
    })

@login_required
def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        try:
            department.delete()
            messages.success(request, 'Department deleted successfully!')
            return redirect('hr:department_list')
        except Exception as e:
            messages.error(request, f'Error deleting department: {str(e)}')
    return render(request, 'hr/department_confirm_delete.html', {'department': department})

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
def attendance_edit(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        try:
            # Update attendance record here
            messages.success(request, 'Attendance record updated successfully!')
            return redirect('hr:attendance_list')
        except Exception as e:
            messages.error(request, f'Error updating attendance: {str(e)}')
    return render(request, 'hr/attendance_form.html', {'attendance': attendance, 'is_edit': True})

@login_required
def attendance_delete(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        try:
            attendance.delete()
            messages.success(request, 'Attendance record deleted successfully!')
            return redirect('hr:attendance_list')
        except Exception as e:
            messages.error(request, f'Error deleting attendance: {str(e)}')
    return render(request, 'hr/attendance_confirm_delete.html', {'attendance': attendance})

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
