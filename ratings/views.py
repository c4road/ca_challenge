from rest_framework import generics, status
from rest_
from .serializers import RatingSerializer
from .models import Rating
from .renderers import RatingJSONRenderer

from authentication.models import User
from companies.models import Company

# Create your views here.


class RatingRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object() # here the object is retrieved
        serializer = self.get_serializer(instance)

        return Response(serializer.data, status=status.HTTP_200_OK)




class RatingListCreateAPIView(generics.ListCreateAPIView):
 
	lookup_field = 'reviewer'
	lookup_url_kwarg = 'reviewer_id'
	permission_classes = (IsAuthenticated,)
	queryset = Rating.objects.select_related(
		'reviewer')

	renderer_classes = (RatingJSONRenderer,)
	serializer_class = RatingSerializer


	def filter_queryset(self, queryset):
		# The built-in list function calls `filter_queryset`. Since we only
		# want comments for a specific article, this is a good place to do
		# that filtering.

		filters = {self.lookup_field: self.kwargs[self.lookup_url_kwarg]}

		return queryset.filter(**filters)


	def create(self, request, reviewer_id=None):

		data = request.data.get('rating', {})
		context = {'author': request.user.profile}

		try: 
			context['article'] = User.objects.get(id=reviewer_id)
			
		except User.DoesNotExist:
			raise NotFound('A user with this id does not exists')

		try: 
			context['company'] = Company.objects.get(id=self.kwargs['company_id'])
			
		except Company.DoesNotExist:
			raise NotFound('A company with that id does not exists')


		
		serializer = self.serializer_class(data=data, context=context)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response(serializer.data, status=status.HTTP_201_CREATED)

