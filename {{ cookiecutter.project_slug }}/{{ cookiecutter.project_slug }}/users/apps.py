from django.apps import AppConfig


class ExempleConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "{{ cookiecutter.project_slug }}.users"
