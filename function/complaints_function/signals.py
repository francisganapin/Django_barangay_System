from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Complaints_model
from function.resident_function.models import Residents_model
from django.apps import apps


#we use this for initial input on our database 




@receiver(post_migrate)
def create_default_resident(sender, **kwargs):
    if sender.name != 'function.complaints_function':  # Ensure correct app name
        return
    
    Complaints_model = apps.get_model('complaints_function','Complaints_model')

    complaints_default = [
    {
        "complaint_id": 1,
        "resident": 1,
        "complaint_date": "2024-02-01",
        "description": "Water supply issue in the area.",
        "status": "Pending"
    },
    {
        "complaint_id":2,
        "resident": 2,
        "complaint_date": "2024-02-05",
        "description": "Street lights not working.",
        "status": "In Progress"
    },
    {
        "complaint_id": 3,
        "resident": 3,
        "complaint_date": "2024-02-10",
        "description": "Garbage collection delay.",
        "status": "Resolved"
    },
    {
        "complaint_id": 4,
        "resident": 4,
        "complaint_date": "2024-02-12",
        "description": "Noise complaint from neighbors.",
        "status": "Pending"
    },
    {
        "complaint_id": 5,
        "resident": 5,
        "complaint_date": "2024-02-15",
        "description": "Road repair needed near my house.",
        "status": "In Progress"
    }
]



    for data_complaints in complaints_default:

        insitance_resident = Residents_model.objects.get(pk=data_complaints['resident']) # initialize the complaint

        Complaints_model.objects.get_or_create(
           complaint_id=data_complaints['complaint_id'],
                defaults={
                    'resident': insitance_resident,  # Assign instance, not just an ID
                    'complaint_date': data_complaints['complaint_date'],
                    'description': data_complaints['description'],
                    'status': data_complaints['status']
                }
            )
      
    
            
        