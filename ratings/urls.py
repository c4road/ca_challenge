from django.urls import path, re_path

from rest_framework.routers import DefaultRouter

from .views import (

	RatingRetrieveAPIView,
	RatingListCreateAPIView,
	RatingAdminAPIView,

)


urlpatterns = [
	
	re_path(r'^company/(?P<company_id>[\d]+)/ratings/$', RatingListCreateAPIView.as_view(), name='create-list'),
	re_path(r'^ratings/(?P<rating_id>[\d]+)/$', RatingRetrieveAPIView.as_view(), name='create-list'),
	re_path(r'^ratings/list/$', RatingAdminAPIView.as_view(), name='create-list'),

]

