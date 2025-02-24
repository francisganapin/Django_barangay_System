from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def create_default_resident(sender, **kwargs):
    if sender.name != 'function.services_function':  # Ensure correct app name
        return
    
    Service_model = apps.get_model('services_function','Service_model')

    service_sample =  [
            {
                "service_id": 1,
                "service_name": "Consultation",
                "description": "An in-depth consultation session.",
                "fee": 100.00
            },
            {
                "service_id": 2,
                "service_name": "Therapy Session",
                "description": "A one-hour therapy session.",
                "fee": 150.00
            },
            {
                "service_id": 3,
                "service_name": "Follow-up",
                "description": "A follow-up session to monitor progress.",
                "fee": 75.00
            }
        ]



    for data_service in service_sample:
        Service_model.objects.get_or_create(
            service_id=data_service['service_id'],
            defaults={
                'service_name':data_service['service_name'],
                'description':data_service['description'],
                'fee':data_service['fee'], 
            }
        )