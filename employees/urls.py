from django.urls import path
from .views import  get_employee, update_employee,employees_view,delete_employee

urlpatterns = [
    path("employees/", employees_view),
    path("employees/<int:emp_id>/", get_employee),
    path("employees/<int:emp_id>/update/", update_employee),
    path("employees/<int:emp_id>/delete/", delete_employee),
]

