from rest_framework import serializers
from imageupload.models import UploadedImage

class UploadedImageSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField("get_username")
    class Meta:
        model = UploadedImage
        fields = ('image_id', 'image', 'username', 'created_date')  # only serialize the primary key and the image field
    
    def get_username(self, obj):
        return obj.owner.username
