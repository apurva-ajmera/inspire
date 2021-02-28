from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django import forms
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    content = RichTextUploadingField(extra_plugins=['youtube',],external_plugin_resources=[('youtube','/static/blog/ckeditor_plugin/youtube/youtube/','plugin.js')])
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:20]

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
