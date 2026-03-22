import os
import django
from django.utils import timezone
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'barangay_system.settings')
django.setup()

from function.resident_function.models import Residents_model
from django.conf import settings

print("Current working directory:", os.getcwd())
print("Database file:", settings.DATABASES['default']['NAME'])
print("Total residents found:", Residents_model.objects.count())

for i, resident in enumerate(Residents_model.objects.all(), start=1):
    old_id = resident.resident_id
    new_id = f"TIBAY-BG-{timezone.now().strftime('%m%d%M%S')}-{i}"
    resident.resident_id = new_id
    resident.save()
    print(f"{i}. OLD: {old_id} → NEW: {new_id}")
    time.sleep(0.1)

print("🎉 Finished script.")
