from django.apps import AppConfig


class ComplaintsFunctionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "function.a4_complaints_function"


    def ready(self):
        import function.a4_complaints_function.signals  # Ensure correct import
