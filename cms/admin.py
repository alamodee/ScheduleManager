from django.contrib import admin
from cms.models import Schedule, Discussion

# Register your models here.

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("id", "EventName", "Date", "Place", "Note",)
    list_display_links = ("id", "EventName",)
admin.site.register(Schedule, ScheduleAdmin)



class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('id', 'discussion',)
    list_display_links = ('id', 'discussion',)
admin.site.register(Discussion, DiscussionAdmin)
