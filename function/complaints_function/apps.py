from django.apps import AppConfig


class ComplaintsFunctionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "function.complaints_function"


    def ready(self):
        import function.complaints_function.signals  # Ensure correct import
