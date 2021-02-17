from django.urls import path, include
from registration import views
urlpatterns = [
    path('',views.users_list,name='users_list'),
    path('user/<int:pk>',views.user_detail,name='detail_list')
]
