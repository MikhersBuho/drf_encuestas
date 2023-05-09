from django.apps import AppConfig


class ApiEncuestasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_encuestas'

    def ready(self):
        print("entre al metodo de apps")
        import api_encuestas.signals