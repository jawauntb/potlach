from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group


# Create your models here.
class Bucket(models.Model):
    bucket_name = models.TextField(max_length=40)
    createdate = timezone.datetime.now()
    owner = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.bucket_name


class Item(models.Model):
    item_name = models.TextField(max_length=40)
    createdate = timezone.datetime.now()
    item_img = models.ImageField
    owner = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    bucket = models.OneToOneField(Bucket, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name







