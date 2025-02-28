from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def create_default_resident(sender, **kwargs):
    if sender.name != 'function.annoucement_function':  # Ensure correct app name
        return
    
    Announcement_model = apps.get_model('annoucement_function','Announcement_model')



    announcement_data = [
    {
        "title": "Community Meeting",
        "content": "There will be a community meeting on March 5th to discuss upcoming projects.",
        "published_date": "2025-02-27",
        "expiry_date": "2025-03-10",
        "is_active": True
    },
    {
        "title": "New Park Opening",
        "content": "Join us for the grand opening of the new community park on April 15th. Refreshments will be provided.",
        "published_date": "2025-03-01",
        "expiry_date": "2025-04-16",
        "is_active": True
    },
    {
        "title": "Library Closure",
        "content": "The community library will be closed for renovations from May 1st to June 30th.",
        "published_date": "2025-04-10",
        "expiry_date": "2025-06-30",
        "is_active": True
    }
    ]


    for data in announcement_data:
            Announcement_model.objects.get_or_create(
                title=data['title'],
                defaults={
                    'content':data['content'],
                    'published_date': data['published_date'], 
                    'expiry_date':data['expiry_date'],
                    'is_active':data['is_active']
                }
            )