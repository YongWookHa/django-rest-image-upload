from rest_framework import viewsets, status
from rest_framework.response import Response

from imageupload_rest.serializers import UploadedImageSerializer
from imageupload.models import UploadedImage 
from user_model_customize.models import User
from django.core.files.base import ContentFile

import base64
import numpy as np
import cv2

def decode_image_from_string(image_string) -> 'numpy image':
    nparr = np.frombuffer(base64.decodebytes(image_string.encode('utf8')), np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR)

class UploadedImagesViewSet(viewsets.ModelViewSet):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadedImageSerializer

    def post(self, request):
        image_string = request.data['base64']
        format, imgstr = image_string.split(';base64,')
        ext = format.split('/')[-1]
        request.data['image'] = ContentFile(base64.b64decode(imgstr), name='filename.'+ext)
        request.data['owner'] = User.objects.get(api_key=request.data['api_key']).pk
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()