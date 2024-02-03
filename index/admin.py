from django.contrib import admin
from index.models import *

# Register your models here.
class SocialAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status")
    list_display_links = ("id","title")
    list_editable = ("status",)
    search_fields = ("title",)



admin.site.register(Social, SocialAdmin)