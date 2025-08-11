from django.db import models
from django.contrib.auth.models import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User on_delete=models.CASCADE, related_name='profile')
    id_user = models.IntegerField()
    bio = models.TextField(blank=True, null=True)
    profileimg = models.ImageField(upload_to ='profile_images', default='blank-profile-picture.jpg')
    location = pass
    