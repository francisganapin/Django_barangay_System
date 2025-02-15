from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Residents_model
from django.apps import apps

@receiver(post_migrate)
def create_default_resident(sender, **kwargs):
    if sender.name != 'function.resident_function':  # Ensure correct app name
        return
    
    Residents_model = apps.get_model('resident_function','Residents_model')

    resident_defaults = [
    {
        "resident_id": "RES001",
        "first_name": "Juan",
        "last_name": "Dela Cruz",
        "birth_date": "1990-05-15",
        "address": "123 Rizal St, Manila",
        "contact_number": "09123456789",
        "house_id": "H001",
        "gender": "Male"
    },
    {
        "resident_id": "RES002",
        "first_name": "Maria",
        "last_name": "Santos",
        "birth_date": "1985-09-22",
        "address": "456 Bonifacio Ave, Quezon City",
        "contact_number": "09234567890",
        "house_id": "H002",
        "gender": "Female"
    },
    {
        "resident_id": "RES003",
        "first_name": "Carlos",
        "last_name": "Reyes",
        "birth_date": "1995-12-10",
        "address": "789 Mabini St, Pasig",
        "contact_number": "09345678901",
        "house_id": "H003",
        "gender": "Male"
    },
    {
        "resident_id": "RES004",
        "first_name": "Ana",
        "last_name": "Lopez",
        "birth_date": "2000-07-30",
        "address": "101 Luna St, Makati",
        "contact_number": "09456789012",
        "house_id": "H004",
        "gender": "Female"
    },
    {
        "resident_id": "RES005",
        "first_name": "Pedro",
        "last_name": "Gomez",
        "birth_date": "1988-03-25",
        "address": "202 Katipunan Rd, Marikina",
        "contact_number": "09567890123",
        "house_id": "H005",
        "gender": "Male"
    }
]


    for data_resident in resident_defaults:
        Residents_model.objects.get_or_create(
            resident_id=data_resident['resident_id'],
            defaults={
                'first_name':data_resident['first_name'],
                'last_name':data_resident['last_name'],
                'birth_date': data_resident['birth_date'], 
                'address':data_resident['address'],
                'contact_number':data_resident['contact_number'],
                'house_id':data_resident['house_id'],
                'gender':data_resident['gender']

            }
        )