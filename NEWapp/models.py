from django.db import models
from django.contrib.auth.models import User

# Create your models here.makemigrations

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Document(models.Model):
    contactholder = models.ForeignKey(User,on_delete=models.CASCADE,default=True)
    title=models.CharField(max_length=255)
    content=models.TextField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('title',)