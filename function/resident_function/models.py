from django.db import models

class Residents_model(models.Model):
    resident_id = models.CharField(max_length=15,unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    address = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=12)
    house_id = models.CharField(max_length=12)
    gender = models.CharField(max_length=12)

    class Meta:
        db_table = 'resident_table'

    def __str__(self):
        return f"{self.resident_id} - {self.first_name} - {self.last_name}"