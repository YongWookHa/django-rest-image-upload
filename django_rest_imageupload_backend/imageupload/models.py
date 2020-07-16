from django.db import models
from django.conf import settings
import uuid

def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(instance.id, extension)

# Create your models here.
class UploadedImage(models.Model):
    image_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField("Uploaded image", upload_to=scramble_uploaded_filename)  # stores the filename of an uploaded image
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)