from django.db import models

class Announcement_model(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'announcement_table'
