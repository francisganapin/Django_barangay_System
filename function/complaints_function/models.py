from django.db import models

# Create your models here.
from function.resident_function.models import Residents_model

class Complaints_model(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    resident = models.ForeignKey(Residents_model,on_delete=models.CASCADE)
    complaint_date = models.DateField()
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[('Pending','pending'),('In Progress','In Progress'),('Resolved','resolved')],
        default="Pending",
    )
    archive = models.BooleanField(default=False)


    class Meta:
        db_table = 'complaints_table'



    def __str__(self):
        return f"Complaint {self.complaint_id} - {self.status}"