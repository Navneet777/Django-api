from django.urls import path
from .views import GameStoreAPIView

urlpatterns = [
    path('', GameStoreAPIView.as_view()),
    path('<int:id>', GameStoreAPIView.as_view()),
]
