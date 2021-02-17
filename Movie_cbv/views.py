from django.shortcuts import render
from .models import Movie_Model
from .serializers import Movie_ModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MovieAPIView(APIView):

    def get(self, request):
        movies = Movie_Model.objects.all()
        serializer = Movie_ModelSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Movie_ModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDetails(APIView):

    def get_object(self, id):
        try:
            return Movie_Model.objects.get(id=id)
        except Movie_Model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        movies = self.get_object(id)
        serializer = Movie_ModelSerializer(movies)
        return Response(serializer.data)

    def put(self, request,id):
        movies = self.get_object(id)
        serializer = Movie_ModelSerializer(movies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        movies = self.get_object(id)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
