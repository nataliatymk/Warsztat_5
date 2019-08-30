from django.contrib.auth.models import User
from django.db import models

class Photo(models.Model):
    path = models.CharField(max_length=512)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media")


    def __str__(self):
        return self.path


class Likes(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)