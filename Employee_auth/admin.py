from django.contrib import admin
from Employee_auth.models import Employee_Model
# Register your models here.
class Employee_ModelAdmin(admin.ModelAdmin):
    list_display = ['employee_id','employee_name','designation','department','email','phone','salary','create_date']

admin.site.register(Employee_Model,Employee_ModelAdmin)
admin.site.site_header = 'Employee Database'
