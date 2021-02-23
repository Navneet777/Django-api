from django.shortcuts import render
# Create your views here.
from .models import Employee_Model
from .serializers import Employee_ModelSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class EmployeeAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = Employee_ModelSerializer
    queryset = Employee_Model.objects.all()
    lookup_field = 'employee_id'
    # Generated token bcae7daf6eba444efebd03f7e0a15e2cb73fa155 for user navneet
    # authentication_classes = [BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, employee_id = None):

        if employee_id:
            return self.retrieve(request)

        else:
           return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, employee_id=None):
        return self.update(request, employee_id)

    def delete(self, request, employee_id):
        return self.destroy(request, employee_id)
