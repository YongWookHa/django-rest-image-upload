from rest_framework import serializers
from imageupload.models import UploadedImage

class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ('id', 'image', 'owner', 'created_date')  # only serialize the primary key and the image field
