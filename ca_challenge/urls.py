from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/', include(('authentication.urls','authentication'), namespace='auth')),
    path(r'api/', include(('ratings.urls','ratings'), namespace='ratings')),
    path(r'api/', include(('companies.urls','companies'), namespace='companies')),

]

