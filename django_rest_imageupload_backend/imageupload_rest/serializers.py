from rest_framework import serializers
from imageupload.models import UploadedImage
from user_model_customize.models import User

class UploadedImageSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField("get_username")
    api_key = serializers.CharField(write_only=True)
    class Meta:
        model = UploadedImage
        read_only_fields = ['owner', ]
        fields = ['image_id', 'image', 'owner', 'created_date', 'api_key',]  # only serialize the primary key and the image field

    def create(self, validated_data):
        validated_data['owner'] = User.objects.get(api_key=validated_data['api_key'])
        validated_data.pop('api_key', None)
        return super().create(validated_data)

    def get_username(self, obj):
        return obj.owner.username