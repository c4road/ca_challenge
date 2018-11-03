from django.urls import re_path

from .views import (

	ReviewRetrieveAPIView,
	ReviewListCreateAPIView,
	ReviewAdminAPIView,

)


urlpatterns = [
	
	re_path(r'company/(?P<company_id>[\d]+)/ratings/', ReviewListCreateAPIView.as_view(), name='create-list'),
	re_path(r'ratings/(?P<rating_id>[\d]+)/', ReviewRetrieveAPIView.as_view(), name='retrieve'),
	re_path(r'ratings/list/', ReviewAdminAPIView.as_view(), name='admin-list'),
	
]

