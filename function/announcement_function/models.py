from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)