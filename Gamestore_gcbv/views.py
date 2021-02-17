from django.shortcuts import render
from .models import Game_store_Model
from .serializers import Game_store_ModelSerializer
from rest_framework import generics
from rest_framework import mixins

class GameStoreAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = Game_store_ModelSerializer
    queryset = Game_store_Model.objects.all()
    lookup_field = 'id'


    def get(self, request, id=None):

        if id:
            return self.retrieve(request)
        else:
           return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)
