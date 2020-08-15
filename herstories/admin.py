from django.contrib import admin
from .models import Herstory

class HerstoryAdminInline(admin.TabularInline):
    model = Herstory

class HerstoryAdmin(admin.HerstoryAdmin):

    fields = ('full_name', 'age', 'occupation', 'story',)

    list_display = ('full_name', 'age', 'occupation', 'story',)

admin.site.register(Herstory, HerstoryAdmin)