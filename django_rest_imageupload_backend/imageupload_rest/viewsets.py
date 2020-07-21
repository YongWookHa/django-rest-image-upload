from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from imageupload_rest.serializers import UploadedImageSerializer
from imageupload.models import UploadedImage 
from user_model_customize.models import User
from django.core.files.base import ContentFile
from django.http import QueryDict

import base64
# import numpy as np
# import cv2

from ocr_engine.detector import TextDetector
from ocr_engine.cluster import FeatureExtractor
from ocr_engine.utils import decode_image_from_string, get_logger

def decode_image_from_string(image_string) -> 'numpy image':
    nparr = np.frombuffer(base64.decodebytes(image_string.encode('utf8')), np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR)

class UploadedImagesViewSet(viewsets.ModelViewSet):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadedImageSerializer

    def post_images(self, request):
        new_req_dict = dict()
        new_req_dict['owner'] = User.objects.get(api_key=request.data['api_key']).pk
        request.data.update(new_req_dict)

        return self.create(request)
    
    def post_base64(self, request):
        base64img = request.data['image']
        if not isinstance(base64img, str):
            raise ValidationError(
            'Invalid value: {}, expected base64 encoded image'.format(base64img)
            )
        format, imgstr = base64img.split(';base64,')
        ext = format.split('/')[-1]
        new_req_dict = dict()
        new_req_dict['image'] = ContentFile(base64.b64decode(imgstr), name='filename.'+ext)
        new_req_dict['owner'] = User.objects.get(api_key=request.data['api_key']).pk
        request.data.update(new_req_dict)

        return self.create(new_req_dict)
