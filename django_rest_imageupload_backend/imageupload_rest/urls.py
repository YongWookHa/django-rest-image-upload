from django.conf.urls import url, include
from rest_framework import routers
from imageupload_rest.viewsets import UploadedImagesViewSet

# router = routers.DefaultRouter()
# router.register('images', UploadedImagesViewSet, 'images')

# Wire up our API using automatic URL routing
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # url(r'', include(router.urls)),
    url(r'^images', UploadedImagesViewSet.as_view({'get': 'list', 'post': 'post_images'}), name='images'),
    url(r'^base64', UploadedImagesViewSet.as_view({'get': 'list', 'post': 'post_base64'}), name='base64')
]