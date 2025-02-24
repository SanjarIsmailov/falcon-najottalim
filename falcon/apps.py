from django.apps import AppConfig

class FalconConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'falcon'

    def ready(self):
        import falcon.signals