from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    cím = models.CharField(max_length=100)
    tartalom = RichTextUploadingField()
    kelt = models.DateTimeField(default=timezone.now)
    szerző = models.ForeignKey(User, on_delete=models.CASCADE)
    intro = models.CharField(max_length=100, default='intro')
    kép = models.ImageField(default='pdefault.png', upload_to='post_pics')

    def __str__(self):
        return self.cím

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
