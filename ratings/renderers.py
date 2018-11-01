from core.renderers import ConduitJSONRenderer


class RatingJSONRenderer(ConduitJSONRenderer):

	object_label = 'rating'
	# object_label_plural = 'articles' ### This was changed when configuring pagination in core renderers
	# pagination_object_label = 'articles'
	# pagination_count_label = 'articlesCount'
