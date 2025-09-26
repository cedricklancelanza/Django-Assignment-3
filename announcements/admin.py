from django.contrib import admin
from .models import Announcement

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")   # columns in the admin list view
    search_fields = ("title", "content")     # adds a search bar
