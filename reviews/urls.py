from django.urls import re_path, path

from .views import (

	ReviewRetrieveAPIView,
	CompanyReviewCreateAPIView,
	ReviewAdminAPIView,
	ReviewOwnerListAPIView,

)


urlpatterns = [
	
	re_path(r'reviews/company/(?P<company_id>[\d]+)/', CompanyReviewCreateAPIView.as_view(), name='create'),
	path(r'reviews/', ReviewOwnerListAPIView.as_view(), name='owner-list'),
	re_path(r'reviews/(?P<review_id>[\d]+)/', ReviewRetrieveAPIView.as_view(), name='retrieve'),
	path(r'admin/reviews/', ReviewAdminAPIView.as_view(), name='admin-list'),
	
]

