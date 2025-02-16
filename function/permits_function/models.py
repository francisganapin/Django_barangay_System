from django.db import models
from resident_function.models import Residents_model

# Create your views here.
class Permit(models.Model):
    permit_type = models.Charfield(max_lenght=100)
    issued_date = models.DateField()
    expiration_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[('Pending','pending'),('Approve','Approve'),('Rejected','rejected')],
        default="Pending",
    )
    resident = models.ForeignKey(Residents_model,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.permit_type} - {self.resident.first_name}'