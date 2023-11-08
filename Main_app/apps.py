from django.apps import AppConfig


class MainAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Main_app'

    def ready(self):
        from .tools import Integrations, Metrics, Settings
        self.Integrations = Integrations
        self.Metrics = Metrics
        self.Settings = Settings
