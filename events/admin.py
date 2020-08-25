from django.contrib import admin
from .models import Event


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'location',
        'distance',
        'description',
        'image',
    )


admin.site.register(Event, EventAdmin)
