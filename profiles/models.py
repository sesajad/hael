from datetime import timedelta

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser


class IpSpec(models.Model):
    owner = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE)
    address = models.CharField(max_length=20)
    expire_time = models.DateTimeField()

    def save(self, *args, **kwargs):
        now = timezone.now() + timedelta(days=1)
        self.expire_time = now
        super(IpSpec, self).save(*args, **kwargs)


class Profile(AbstractUser):
    max_ip = models.SmallIntegerField(default=2)
