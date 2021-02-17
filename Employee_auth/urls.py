from django.urls import path
from .views import EmployeeAPIView

urlpatterns = [
    path('', EmployeeAPIView.as_view()),
    path('<int:employee_id>', EmployeeAPIView.as_view()),
]
