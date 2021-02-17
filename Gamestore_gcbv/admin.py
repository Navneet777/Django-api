from django.contrib import admin
from Gamestore_gcbv.models import Game_store_Model
# Register your models here.
class Game_store_ModelAdmin(admin.ModelAdmin):
    list_display = ['id','game_name','category','rating','price']


admin.site.register(Game_store_Model,Game_store_ModelAdmin)
