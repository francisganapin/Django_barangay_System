from django.db import models
from function.resident_function.models import Residents_model

class Service_model(models.Model):
    service_name = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    fee = models.DecimalField(max_digits=6,decimal_places=2)

    class Meta:
        db_table = 'service_table'

    def __str__(self):
        return f'{self.service_name} -{self.fee}'
    


class ResidentServiceAvail(models.Model):
    resident_id = models.ForeignKey(Residents_model,on_delete=models.CASCADE)
    service_avail = models.ForeignKey(Service_model,on_delete=models.CASCADE)


class Permit_mode(models.Model):
    permit_id = models.AutoField(primary_key=True)
    resident_id = models.ForeignKey(Residents_model,on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service_model,on_delete=models.CASCADE)
    application_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[('Pending','pending'),('Approve','Approve'),('Rejected','rejected')],
        default="Pending",
    )
    
    class Meta:
        db_table = 'permits_table'

    def __str__(self):
        return f"Permit {self.permit_id} - {self.status}"