from django.urls import path
from .views import (
    {{ cookiecutter.app_name }}CreateView,
    {{ cookiecutter.app_name }}UpdateView,
    {{ cookiecutter.app_name }}DeleteView,
    {{ cookiecutter.app_name }}DetailView,
    {{ cookiecutter.app_name }}ListView,
)

app_name = "{{ cookiecutter.app_name }}"

urlpatterns = [
    path("", {{ cookiecutter.app_name }}ListView.as_view(), name="{{ cookiecutter.app_name }}_list"),
    path("create/", {{ cookiecutter.app_name }}CreateView.as_view(), name="{{ cookiecutter.app_name }}_create"),
    path("<int:pk>/", {{ cookiecutter.app_name }}DetailView.as_view(), name="{{ cookiecutter.app_name }}_detail"),
    path("<int:pk>/update/", {{ cookiecutter.app_name }}UpdateView.as_view(), name="{{ cookiecutter.app_name }}_update"),
    path("<int:pk>/delete/", {{ cookiecutter.app_name }}DeleteView.as_view(), name="{{ cookiecutter.app_name }}_delete"),
]
