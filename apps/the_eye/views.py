from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from .serializers import EventSerializer
from .models import Event




class EventViewSet(viewsets.ModelViewSet):
	
	serializer_class = EventSerializer
	queryset = Event.objects.all().order_by('timestamp')

	def get_queryset(self):
		
		return Event.objects.all()