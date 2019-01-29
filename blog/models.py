from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from tinymce.models import HTMLField

class Post(models.Model):
    cim = models.CharField(max_length=100)
    tartalom = HTMLField()
    kelt = models.DateTimeField(default=timezone.now)
    szerzo = models.ForeignKey(User, on_delete=models.CASCADE)
    intro = models.CharField(max_length=100, default='intro')
    kep = models.ImageField(default='pdefault.png', upload_to='post_pics')
    megtekintes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.cim

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
