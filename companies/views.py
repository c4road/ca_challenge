from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import (

	AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
)
from rest_framework.response import Response
from .serializers import CompanySerializer
from .renderers import CompaniesJSONRenderer
# Create your views here.


class CompanyCreateView(generics.CreateAPIView):
    serializer_class = CompanySerializer
    permission_classes = (AllowAny,)
    renderer_classes = (CompaniesJSONRenderer,)


