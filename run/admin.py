from django.contrib import admin
from .models import Run


# Register your models here.
class RunAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'location',
        'distance',
        'description',
        'image',
    )


admin.site.register(Run, RunAdmin)
