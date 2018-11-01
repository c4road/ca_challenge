from django.urls import path, re_path

from rest_framework.routers import DefaultRouter

from .views import (

	RatingRetrieveAPIView,
	RatingListCreateAPIView

)


urlpatterns = [
	
	re_path(r'^ratings/(?P<reviewer_id>[\d]+)/(?P<comment_pk>[\d]+)$', RatingListCreateAPIView.as_view(), name='verificate'),

]

