from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class user(User):
    crypto_wallet = models.CharField(max_length=200)
    points = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.username + ' | ' + self.crypto_wallet 
    class Meta:
        verbose_name_plural = "User"
#_____________________________________________________#
