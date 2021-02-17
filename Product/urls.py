from django.urls import path
from Product import views
urlpatterns = [
    path('',views.product_list,name='product_list'),
    path('<int:pk>',views.product_detail,name='product_detail')

]
