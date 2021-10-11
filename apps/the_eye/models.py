from django.db import models
from django.utils import timezone 

from rest_framework_api_key.models import AbstractAPIKey


class Application(models.Model):
	"""
	Application Model
	"""
	name = models.CharField(max_length=50, blank=True)
	host = models.URLField(null=True, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name


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
	session_id = models.UUIDField(db_index=True, editable=False, null=False, blank=False, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.session_id

class Category(models.Model):

	class Meta:
		verbose_name_plural = "Categories"

	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Event(models.Model):
	"""
	An Event has a category, a name and a payload of data (the payload can change according to which event an Application is sending)
	Different types of Events (identified by category + name) can have different validations for their payloads
	An Event is associated to a Session
	Events in a Session should be sequential and ordered by the time they occurred
	"""
	class EventName(models.TextChoices):
    
	    SUBMIT = "submit", "Submit"
	    PAGEVIEW = "pageview", "Pageview"
	    CTA_CLICK = "cta click", "CTA Click"

	category = models.ForeignKey(Category, related_name="events", on_delete=models.CASCADE)
	name = models.CharField(max_length=10, choices=EventName.choices)
	application = models.ForeignKey(Application, related_name="events", on_delete=models.CASCADE)
	session = models.ForeignKey(Session, related_name="events", on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	timestamp = models.DateTimeField()
	payload = models.JSONField()

	def __str__(self):
		return self.name



