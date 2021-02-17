from django.contrib import admin
from registration.models import Registrations
# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['id','token','first_name','last_name','email','password']

admin.site.register(Registrations,RegisterAdmin)
