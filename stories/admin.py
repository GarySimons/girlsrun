from django.contrib import admin
from .models import Story

# Register your models here.

class StoryAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'age',
        'occupation',
        'details',
        'image',
    )


admin.site.register(Story, StoryAdmin)

