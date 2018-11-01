from core.renderers import AppJSONRenderer


class CompaniesJSONRenderer(AppJSONRenderer):

	object_label = 'company'
	# object_label_plural = 'articles' ### This was changed when configuring pagination in core renderers
	# pagination_object_label = 'articles'
	# pagination_count_label = 'articlesCount'
