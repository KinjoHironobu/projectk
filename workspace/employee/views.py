from django.views import generic
from django.urls import reverse_lazy
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
                "pk": employee.pk,
                "employee": employee.name,
                "department": employee.department,
                "age": employee.age(),
                "period": employee.age_group()
            }
            employees_by_department_and_period.append(list_obj)
        context["department_list"] = department_list
        context["period_list"] = period_list
        context["employees_by_department_and_period"] = employees_by_department_and_period
        return context

class AddEmployeeView(generic.CreateView):
    model = Employee
    fields = "__all__"
    success_url = reverse_lazy("employee:index")

class UpdateEmployeeView(generic.UpdateView):
    model = Employee
    fields = "__all__"
    success_url = reverse_lazy("employee:index")