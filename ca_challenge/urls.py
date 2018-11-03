from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

from authentication.backends import JWTAuthentication

schema_view = get_swagger_view(title='Review API')


urlpatterns = [

	path('admin/', admin.site.urls),
	path(r'api/v1/', include(('authentication.urls','authentication'), namespace='auth')),
	path(r'api/v1/', include(('reviews.urls','reviews'), namespace='reviews')),
	path(r'api/v1/', include(('companies.urls','companies'), namespace='companies')),
	path(r'swagger(<format>\.json|\.yaml)', schema_view, name='schema-json'),
	path(r'swagger/', schema_view, name='schema-swagger-ui'),
	path(r'docs/', include_docs_urls(title='Reviews API',authentication_classes=[JWTAuthentication,],permission_classes=[])),
    
]

