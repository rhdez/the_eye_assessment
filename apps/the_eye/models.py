from django.db import models

from rest_framework_api_key.models import AbstractAPIKey


class Application(models.Model):
	"""
	Application Model
	"""
	name = models.CharField(max_length=50, blank=True)
	host = models.URLField(null=True, unique=True)
class ApplicationAPIKey(AbstractAPIKey):
	"""
	Application API Key
	"""
	application = models.ForeignKey(
		Application, 
		on_delete=models.CASCADE, 
		related_name="api_keys" 
		)

class Session(models.Model):
	"""
	Session Models
	"""


class Event(models.Model):
	"""
	An Event has a category, a name and a payload of data (the payload can change according to which event an Application is sending)
	Different types of Events (identified by category + name) can have different validations for their payloads
	An Event is associated to a Session
	Events in a Session should be sequential and ordered by the time they occurred
	"""
	category = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	applications = models.ForeignKey(Application, related_name="applications", on_delete=models.CASCADE)
	sessions = models.ForeignKey(Session, related_name="sessions", on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name