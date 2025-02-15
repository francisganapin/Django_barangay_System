import os
import django

# Set the settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "barangay_system.settings")

# Initialize Django
django.setup()

from barangay_resident.models import Barangay, Resident, Services
from datetime import date

# Create Barangays
barangay1 = Barangay.objects.create(name="Barangay 1", location="Quezon City")
barangay2 = Barangay.objects.create(name="Barangay 2", location="Makati City")

# Create Residents
resident1 = Resident.objects.create(first_name="Juan", last_name="Dela Cruz", email="juan@gmail.com", barangay=barangay1)
resident2 = Resident.objects.create(first_name="Maria", last_name="Santos", email="maria@gmail.com", barangay=barangay1)
resident3 = Resident.objects.create(first_name="Pedro", last_name="Reyes", email="pedro@gmail.com", barangay=barangay2)
resident4 = Resident.objects.create(first_name="Anna", last_name="Gonzales", email="anna@gmail.com", barangay=barangay2)

# Create Services
Services.objects.create(resident=resident1, services_type="Health Check-up", services_data=date(2024, 1, 15))
Services.objects.create(resident=resident1, services_type="Vaccination", services_data=date(2024, 2, 10))
Services.objects.create(resident=resident2, services_type="Financial Assistance", services_data=date(2024, 3, 5))
Services.objects.create(resident=resident2, services_type="Educational Assistance", services_data=date(2024, 4, 20))
Services.objects.create(resident=resident3, services_type="Livelihood Support", services_data=date(2024, 5, 12))
Services.objects.create(resident=resident3, services_type="Senior Citizen Benefits", services_data=date(2024, 6, 8))
Services.objects.create(resident=resident4, services_type="Disaster Relief", services_data=date(2024, 7, 15))
Services.objects.create(resident=resident4, services_type="Housing Assistance", services_data=date(2024, 8, 22))
Services.objects.create(resident=resident1, services_type="Medical Aid", services_data=date(2024, 9, 18))
Services.objects.create(resident=resident3, services_type="Food Assistance", services_data=date(2024, 10, 25))

print("Sample data inserted successfully!")
