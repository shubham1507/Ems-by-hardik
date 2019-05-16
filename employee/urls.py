

from django.urls import path
from employee.views import *

urlpatterns = [
    path('',employee_list, name = 'employee_list'),
    # path('<int:id>/details/', details, name="employee-details"),
    path('add/',employee_add, name="employee_add" )
]
