from django.db import models

# Create your models here.
class Token(models.Model):
    access_token = models.CharField(max_length=255)
    token_type = models.CharField(max_length=10)
    expires_in = models.DateTimeField()
