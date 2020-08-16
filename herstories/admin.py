from django.contrib import admin
from .models import Herstory

class HerstoryAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'age',
        'occupation',
        'story',
    )


admin.site.register(Herstory, HerstoryAdmin)