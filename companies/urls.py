from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import CompanyViewSet

router = DefaultRouter()
router.register(r'company', CompanyViewSet, base_name='company')

urlpatterns = [url(r'^', include((router.urls,'company'))),]
