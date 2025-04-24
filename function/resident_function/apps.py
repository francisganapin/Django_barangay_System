from django.apps import AppConfig

class ResidentFunctionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "function.resident_function"  # Make sure this matches your app name

    def ready(self):
        import  function.resident_function.signals  # Ensure correct import
