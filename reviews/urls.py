from django.urls import re_path, path

from .views import (

	ReviewRetrieveAPIView,
	CompanyReviewCreateAPIView,
	ReviewAdminAPIView,
	ReviewOwnerListAPIView,

)


urlpatterns = [
	
	re_path(r'company/(?P<company_id>[\d]+)/create-review/', CompanyReviewCreateAPIView.as_view(), name='create'),
	path(r'my-reviews/', ReviewOwnerListAPIView.as_view(), name='owner-list'),
	re_path(r'review/(?P<review_id>[\d]+)/', ReviewRetrieveAPIView.as_view(), name='retrieve'),
	path(r'review/list/', ReviewAdminAPIView.as_view(), name='admin-list'),
	
]

