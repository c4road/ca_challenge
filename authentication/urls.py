from django.urls import include, path
from django.conf.urls import url
from .views import (

	LoginAPIView, 
	RegistrationAPIView, 
)


urlpatterns = [
	
    url(r'users/?$', RegistrationAPIView.as_view(),name='register'),
    url(r'users/login/?$', LoginAPIView.as_view(),name='login'),
   
]
