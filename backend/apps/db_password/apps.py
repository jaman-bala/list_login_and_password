from django.apps import AppConfig


class DbPasswordConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.apps.db_password'
    verbose_name = 'База паролей'
