from datetime import date
from .models import Complaints_model

sample_complaints = [
    Complaints_model(resident_id=1, complaint_date=date(2025, 1, 5), description="Leaking faucet in kitchen", status="Pending"),
    Complaints_model(resident_id=2, complaint_date=date(2025, 1, 10), description="Noisy neighbors at night", status="In Progress"),
    Complaints_model(resident_id=3, complaint_date=date(2025, 1, 15), description="Broken elevator", status="Resolved"),
    Complaints_model(resident_id=4, complaint_date=date(2025, 2, 1), description="Pest infestation in unit", status="Pending"),
    Complaints_model(resident_id=5, complaint_date=date(2025, 2, 5), description="Water supply issue", status="Resolved"),
    Complaints_model(resident_id=1, complaint_date=date(2025, 2, 10), description="Security gate malfunction", status="In Progress"),
    Complaints_model(resident_id=2, complaint_date=date(2025, 2, 15), description="Parking space dispute", status="Pending"),
    Complaints_model(resident_id=3, complaint_date=date(2025, 3, 1), description="Air conditioning not working", status="Resolved"),
    Complaints_model(resident_id=4, complaint_date=date(2025, 3, 5), description="Garbage collection delay", status="Pending"),
    Complaints_model(resident_id=5, complaint_date=date(2025, 3, 10), description="Unauthorized construction noise", status="In Progress"),
    Complaints_model(resident_id=1, complaint_date=date(2025, 3, 15), description="Street light not functioning", status="Resolved"),
    Complaints_model(resident_id=2, complaint_date=date(2025, 4, 1), description="Blocked drainage", status="Pending"),
    Complaints_model(resident_id=3, complaint_date=date(2025, 4, 5), description="Cracked wall in hallway", status="In Progress"),
    Complaints_model(resident_id=4, complaint_date=date(2025, 4, 10), description="Noise from nearby construction", status="Resolved"),
    Complaints_model(resident_id=5, complaint_date=date(2025, 4, 15), description="Unclean common areas", status="Pending"),
    Complaints_model(resident_id=1, complaint_date=date(2025, 5, 1), description="Elevator buttons not working", status="In Progress"),
    Complaints_model(resident_id=2, complaint_date=date(2025, 5, 5), description="Broken window in lobby", status="Resolved"),
    Complaints_model(resident_id=3, complaint_date=date(2025, 5, 10), description="Unauthorized pet in unit", status="Pending"),
    Complaints_model(resident_id=4, complaint_date=date(2025, 5, 15), description="Power outage in building", status="Resolved"),
    Complaints_model(resident_id=5, complaint_date=date(2025, 5, 20), description="Graffiti on walls", status="In Progress"),
]