from django.db import models
import random
import string


def generate_short_url():
    chars = string.ascii_letters + string.digits
    short_url = ''.join(random.choices(chars, k=6))
    return short_url


class Url(models.Model):
    long_url = models.URLField(max_length=200)
    short_url = models.CharField(max_length=6, default=generate_short_url, unique=True)
    name = models.CharField(max_length=100)
