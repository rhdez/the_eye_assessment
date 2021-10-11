from django.contrib import admin
from .models import Application, Session, Event, ApplicationAPIKey, Category
from rest_framework_api_key.admin import APIKeyModelAdmin


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
class ApplicationAPIKeyAdmin(APIKeyModelAdmin):
	pass
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	pass