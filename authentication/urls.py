from django.urls import include, path
from django.conf.urls import url
from .views import (

	LoginAPIView, 
	RegistrationAPIView, 
)


urlpatterns = [
	
    url(r'reviewers/?$', RegistrationAPIView.as_view(),name='register'),
    url(r'reviewers/login/?$', LoginAPIView.as_view(),name='login'),
   
]
