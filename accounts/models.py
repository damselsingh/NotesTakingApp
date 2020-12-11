from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class note(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    takenotes = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)