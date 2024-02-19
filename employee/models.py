from django.db import models
from django.urls import reverse

class Employee(models.Model):
    name = models.CharField("名前", max_length=50)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Employee_detail", kwargs={"pk": self.pk})
