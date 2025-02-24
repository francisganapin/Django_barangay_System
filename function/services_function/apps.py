from django.apps import AppConfig


class ServicesFunctionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "function.services_function"
    

    def ready(self):
        import function.services_function.signals  # Ensure correct import
