from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.permissions import (

	AllowAny, 
	IsAuthenticated, 
	IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from .serializers import CompanySerializer
from .renderers import CompaniesJSONRenderer
from .models import Company
# Create your views here.


class CompanyViewSet(viewsets.ModelViewSet):

	serializer_class = CompanySerializer
	permission_classes = (AllowAny,)
	queryset = Company.objects.all()
	renderer_classes = (CompaniesJSONRenderer,)