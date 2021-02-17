from django.contrib import admin
from Movie_cbv.models import Movie_Model
# Register your models here.

class Movie_Model_Admin(admin.ModelAdmin):
    list_display = ['name','genere','price','rating','create_date']



admin.site.register(Movie_Model,Movie_Model_Admin)
