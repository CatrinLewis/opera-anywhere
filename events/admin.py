from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Event


class EventAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)

admin.site.register(Event, EventAdmin)

# Register your models here.
# admin.site.register(Event)
