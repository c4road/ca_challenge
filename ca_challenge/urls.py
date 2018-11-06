from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls

from authentication.backends import JWTAuthentication

schema_view = get_schema_view(
   openapi.Info(
      title="Reviews API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   validators=['flex', 'ssv'],
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [

	path('admin/', admin.site.urls),
	path(r'api/v1/', include(('authentication.urls','authentication'), namespace='auth')),
	path(r'api/v1/', include(('reviews.urls','reviews'), namespace='reviews')),
	path(r'api/v1/', include(('companies.urls','companies'), namespace='companies')),
	url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
	url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
	path(r'docs/', include_docs_urls(title='Reviews API',authentication_classes=[JWTAuthentication,],permission_classes=[])),
    
]

