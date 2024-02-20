from typing import Any
from django.views import generic
from .models import Employee, Department

class IndexView(generic.ListView):
    model = Employee

    def get_context_data(self):
        context = super().get_context_data()
        department_list = Department.objects.all()
        period_list = [1, 2, 3, 4, 5, 6,]
        employees_by_department_and_period = []

        for employee in Employee.objects.all():
            list_obj = {
                "employee": employee.name,
                "department": employee.department,
                "year": employee.age(),
                "period": employee.age_group()
            }
            employees_by_department_and_period.append(list_obj)
        context["department_list"] = department_list
        context["period_list"] = period_list
        context["employees_by_department_and_period"] = employees_by_department_and_period
        return context

    
