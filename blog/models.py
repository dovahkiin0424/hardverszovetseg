from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    cim = models.CharField(max_length=100)
    tartalom = models.TextField()
    kelt = models.DateTimeField(default=timezone.now)
    szerzo = models.ForeignKey(User, on_delete=models.CASCADE)
    intro = models.CharField(max_length=200, default='intro')
    kep = models.ImageField(default='pdefault.png')

    def __str__(self):
        return self.cim

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
