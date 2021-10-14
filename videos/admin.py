from django.contrib import admin
from videos.models import Video

# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_dispay = ['title', 'source', 'slug', ]


admin.site.register(Video, VideoAdmin)
