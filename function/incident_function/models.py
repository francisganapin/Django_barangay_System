from django.db import models
from function.resident_function.models import Residents_model

# Create your models here.
class Incident_models(models.Model):
    incident_id = models.AutoField(primary_key=True)
    resident_id = models.ForeignKey(Residents_model,on_delete=models.CASCADE)
    description = models.TextField(max_length=300)
    incident_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[('Pending','pending'),('Approve','Approve'),('Rejected','rejected')],
        default="Pending",
    )
    
    class Meta:
        db_table = 'permits_table'
