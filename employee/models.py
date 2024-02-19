from django.db import models

class Department(models.Model):
    """ 部署 """
    name = models.CharField("部署名", max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    """ 従業者 """
    name = models.CharField("従業者名", max_length=50)
    department = models.ForeignKey(Department, verbose_name="所属部署", on_delete=models.SET_NULL, blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
