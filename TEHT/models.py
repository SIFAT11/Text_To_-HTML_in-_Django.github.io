from django.db import models
from ckeditor.fields import RichTextField


class Text(models.Model):
    body =RichTextField(blank=True,null=True)