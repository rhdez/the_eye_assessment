from django.contrib import admin
from .models import Application, Session, Event, ApplicationAPIKey

# Register your models here.
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
	pass

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
	pass

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	pass

@admin.register(ApplicationAPIKey)
class ApplicationAPIKeyAdmin(admin.ModelAdmin):
	pass