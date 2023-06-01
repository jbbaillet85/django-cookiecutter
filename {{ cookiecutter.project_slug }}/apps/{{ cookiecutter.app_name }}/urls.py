from django.urls import path

app_name = "{{ cookiecutter.app_name }}"

urlpatterns = [
    path("", name="{{ cookiecutter.app_name }}"),
]
