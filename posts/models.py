from django.db import models

# Create your models here.

class Post(models.Model):
    battletag = models.CharField(max_length=25)
    personal_sr = models.CharField(max_length=12)
    role = models.CharField(max_length=8)
    lobby_sr = models.CharField(max_length=12)
    replay_code = models.CharField(max_length=6)
    details = models.CharField(max_length=100)
