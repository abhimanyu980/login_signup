from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class History(models.Model):
    username = models.CharField(max_length=100)
    time = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.email