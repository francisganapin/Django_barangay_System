from django.db import models
from django.utils import timezone


class Residents_model(models.Model):
    resident_id = models.CharField(max_length=50,unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    address = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=12)
    house_id = models.CharField(max_length=12)
    gender = models.CharField(max_length=12)
    is_archive = models.BooleanField(default=False)

    class Meta:
        db_table = 'resident_table'


    def save(self,*args,**kwargs):
        if not self.resident_id:
            resident = 'TIBAY-BG'
            timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
            self.resident_id = f'{resident}-{timestamp}'
        super().save(*args,**kwargs)



    def __str__(self):
        return f"{self.resident_id} - {self.first_name} - {self.last_name}"