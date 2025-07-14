from django.urls import path
from . import views

app_name = 'hr'

urlpatterns = [
    path('', views.hr_dashboard, name='dashboard'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.employee_add, name='employee_add'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/add/', views.department_add, name='department_add'),
    path('departments/<int:pk>/', views.department_detail, name='department_detail'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/add/', views.attendance_add, name='attendance_add'),
    path('leave-requests/', views.leave_request_list, name='leave_request_list'),
    path('leave-requests/add/', views.leave_request_add, name='leave_request_add'),
    path('leave-requests/<int:pk>/', views.leave_request_detail, name='leave_request_detail'),
    path('payroll/', views.payroll_list, name='payroll_list'),
    path('payroll/add/', views.payroll_add, name='payroll_add'),
    path('payroll/<int:pk>/', views.payroll_detail, name='payroll_detail'),
    path('performance/', views.performance_review_list, name='performance_review_list'),
    path('performance/add/', views.performance_review_add, name='performance_review_add'),
    path('performance/<int:pk>/', views.performance_review_detail, name='performance_review_detail'),
    path('training/', views.training_list, name='training_list'),
    path('training/add/', views.training_add, name='training_add'),
    path('training/<int:pk>/', views.training_detail, name='training_detail'),
]
