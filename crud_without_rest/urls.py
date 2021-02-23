from django.urls import path
from crud_without_rest import views

urlpatterns = [
 path('', views.EmployeeCRUDCBV.as_view()),
]
