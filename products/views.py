from django.shortcuts import render

from .serializers import *
from .models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class UserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        print(request.user)
        return Response({'sucess': "hurray you are authenticated" })


class ProductView(APIView):

    def get(self,request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset , many=True)
        return Response(serializer.data)


