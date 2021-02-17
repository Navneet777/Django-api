from django.urls import path
from .views import MovieAPIView, MovieDetails

urlpatterns = [
    path('', MovieAPIView.as_view()),
    path('<int:id>', MovieDetails.as_view()),
]
