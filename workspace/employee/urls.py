from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add-employee/', views.AddEmployeeView.as_view(), name='addEmployee'),
    path('update-employee/<int:pk>/', views.UpdateEmployeeView.as_view(), name='updateEmployee'),
]