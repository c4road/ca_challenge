from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import (IsAuthenticated, IsAdminUser,)
from rest_framework.response import Response

from .serializers import RatingSerializer
from .models import Rating
from .renderers import RatingJSONRenderer
from .permissions import IsOwner

from authentication.models import User
from companies.models import Company

# Create your views here.

class RatingAdminAPIView(generics.ListAPIView):
	queryset = Rating.objects.all()
	permission_classes = (IsAdminUser, IsOwner,)
	serializer_class = RatingSerializer



class RatingRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    lookup_url_kwarg = 'rating_id'
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticated, IsOwner,)



class RatingListCreateAPIView(generics.ListCreateAPIView):
 
	lookup_field = 'reviewer'
	lookup_url_kwarg = 'company_id'
	permission_classes = (IsAuthenticated,)
	queryset = Rating.objects.select_related('reviewer')

	renderer_classes = (RatingJSONRenderer,)
	serializer_class = RatingSerializer


	def filter_queryset(self,queryset):
		
		filters = {'reviewer': self.request.user.id}

		return queryset.filter(**filters)


	def create(self, request, company_id=None):

		data = request.data.get('rating', {})
		context = {'reviewer': request.user}
		x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

		if x_forwarded_for:

		    ip = x_forwarded_for.split(',')[0]
		    context['ip_address'] = ip
		else:
		    ip = request.META.get('REMOTE_ADDR')
		    context['ip_address'] = ip

		try: 
			context['company'] = Company.objects.get(id=company_id)
			
		except Company.DoesNotExist:
			raise NotFound('A company with that id does not exists')

		serializer = self.serializer_class(data=data, context=context)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response(serializer.data, status=status.HTTP_201_CREATED)



