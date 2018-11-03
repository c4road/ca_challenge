from rest_framework import permissions

class IsOwner(permissions.BasePermission):
	""" 
	Check if the user is the instance owner 
	"""
	message = 'Not allowed to see this rating'
	def has_object_permission(self, request, view, obj):

		return obj.reviewer == request.user