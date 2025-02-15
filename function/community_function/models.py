from django.db import models

class Announcement_model(models.Model):
    announcement_id = models.AutoField(primary_key=True)# auto increment id
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    annoucement_date = models.DateField()
    expiry_date = models.DateField()

    class Meta:
        db_table = 'announcement_table'