from django.db import models

class Employee_Model(models.Model):
    employee_id = models.AutoField(primary_key=True,max_length=6)
    employee_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)
    salary = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.employee_name
