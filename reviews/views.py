from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import (IsAuthenticated, IsAdminUser,)
from rest_framework.response import Response

from .serializers import ReviewSerializer
from .models import Review
from .renderers import ReviewJSONRenderer
from .permissions import IsOwner

from authentication.models import Reviewer
from companies.models import Company

# Create your views here.

class CompanyReviewCreateAPIView(generics.CreateAPIView):
 
	lookup_url_kwarg = 'company_id'
	permission_classes = (IsAuthenticated,)
	renderer_classes = (ReviewJSONRenderer,)
	serializer_class = ReviewSerializer


	def create(self, request, company_id=None):

		data = request.data.get('review', {})
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


class ReviewOwnerListAPIView(generics.ListAPIView):

	queryset = Review.objects.all()
	permission_classes = (IsAuthenticated, IsOwner,)
	serializer_class = ReviewSerializer
	renderer_classes = (ReviewJSONRenderer,)

	def filter_queryset(self,queryset):
		
		filters = {'reviewer': self.request.user.id}

		return queryset.filter(**filters)




class ReviewAdminAPIView(generics.ListAPIView):

	queryset = Review.objects.all()
	permission_classes = (IsAdminUser, IsOwner,)
	serializer_class = ReviewSerializer
	renderer_classes = (ReviewJSONRenderer,)



class ReviewRetrieveAPIView(generics.RetrieveAPIView):

    lookup_field = 'id'
    lookup_url_kwarg = 'review_id'
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    renderer_classes = (ReviewJSONRenderer,)
    permission_classes = (IsAuthenticated, IsOwner,)