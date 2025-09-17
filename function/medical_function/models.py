from django.db import models
from function.resident_function.models import Residents_model
# Create your models here.
class Medicine_model(models.Model):
    name = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)
    expiry_date = models.DateField()
    remark = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.stock} pc)"
    


class Appointment_model(models.Model):
    patient = models.ForeignKey(Residents_model,on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100,choices=[
        ('Checkup','Checkup'),
        ('Vaccination','Vaccination'),
        ('Consultation','Consultation'),
        ('Follow-up','Follow-up'),
    ])

    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=20,default='Pending')