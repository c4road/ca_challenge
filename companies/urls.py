from django.urls import path


from .views import (

	CompanyCreateView,

)


urlpatterns = [
	
	path(r'companies/create/', CompanyCreateView.as_view(), name='create'),

]
