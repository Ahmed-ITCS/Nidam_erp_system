from django.contrib import admin
from .models import Department, Position, Employee, Attendance, LeaveType, LeaveRequest, Payroll, PerformanceReview, Training, TrainingEnrollment

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'manager', 'budget', 'is_active']
    search_fields = ['name', 'manager__username']
    list_filter = ['is_active', 'created_at']

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['title', 'department', 'salary_min', 'salary_max', 'is_active']
    search_fields = ['title', 'department__name']
    list_filter = ['is_active', 'created_at']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'user', 'department', 'position', 'employment_status']
    search_fields = ['user__first_name', 'user__last_name', 'employee_id']
    list_filter = ['employment_status', 'employment_type', 'created_at']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['employee', 'date', 'status', 'hours_worked']
    search_fields = ['employee__user__first_name', 'employee__user__last_name']
    list_filter = ['status', 'date', 'created_at']

@admin.register(LeaveType)
class LeaveTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'days_allowed', 'is_paid', 'is_active']
    search_fields = ['name']
    list_filter = ['is_active', 'created_at']

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ['employee', 'leave_type', 'start_date', 'end_date', 'status']
    search_fields = ['employee__user__first_name', 'employee__user__last_name']
    list_filter = ['status', 'start_date', 'end_date', 'created_at']

@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ['employee', 'pay_period_start', 'pay_period_end', 'net_salary', 'status']
    search_fields = ['employee__user__first_name', 'employee__user__last_name']
    list_filter = ['status', 'pay_period_start', 'pay_period_end', 'created_at']

@admin.register(PerformanceReview)
class PerformanceReviewAdmin(admin.ModelAdmin):
    list_display = ['employee', 'review_period_start', 'review_period_end', 'overall_rating']
    search_fields = ['employee__user__first_name', 'employee__user__last_name']
    list_filter = ['review_period_start', 'review_period_end', 'created_at']

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ['title', 'trainer', 'start_date', 'end_date', 'max_participants']
    search_fields = ['title', 'trainer']
    list_filter = ['is_mandatory', 'is_active', 'created_at']

@admin.register(TrainingEnrollment)
class TrainingEnrollmentAdmin(admin.ModelAdmin):
    list_display = ['training', 'employee', 'enrollment_date', 'status']
    search_fields = ['training__title', 'employee__user__first_name', 'employee__user__last_name']
    list_filter = ['status', 'created_at']
