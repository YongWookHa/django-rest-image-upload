from django.contrib import admin
from imageupload.models import UploadedImage

@admin.register(UploadedImage)
class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ['image_id', 'owner', 'created_date' ]
    list_filter = ['owner',]
    search_fields = ['image_id', ]
