from django.db import models
from datetime import date

class Department(models.Model):
    """ 部署 """
    name = models.CharField("部署名", max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    """ 従業者 """
    empno = models.PositiveIntegerField("従業者番号", unique=True, default=0)
    name = models.CharField("従業者名", max_length=50)
    department = models.ForeignKey(Department, verbose_name="所属部署", on_delete=models.SET_NULL, blank=True, null=True, default=None)
    birth_day = models.DateField("生年月日", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def age(self):
        today = date.today()
        return today.year - self.birth_day.year - ((today.month, today.day) < (self.birth_day.month, self.birth_day.day))

    def age_group(self):
        age = self.age()
        return age // 10  # 年齢の一桁目を切り捨てる
