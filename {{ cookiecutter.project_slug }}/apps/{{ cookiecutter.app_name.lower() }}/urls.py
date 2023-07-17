from django.urls import path
from apps.{{ cookiecutter.app_name.lower() }}.views import (
    {{ cookiecutter.app_name.title() }}CreateView,
    {{ cookiecutter.app_name.title() }}UpdateView,
    {{ cookiecutter.app_name.title() }}DeleteView,
    {{ cookiecutter.app_name.title() }}DetailView,
    {{ cookiecutter.app_name.title() }}ListView,
)

app_name = "{{ cookiecutter.app_name }}"

urlpatterns = [
    path("", {{ cookiecutter.app_name.title() }}ListView.as_view(), name="{{ cookiecutter.app_name }}_list"),
    path("create/", {{ cookiecutter.app_name.title() }}CreateView.as_view(), name="{{ cookiecutter.app_name }}_create"),
    path("<int:pk>/", {{ cookiecutter.app_name.title() }}DetailView.as_view(), name="{{ cookiecutter.app_name }}_detail"),
    path("<int:pk>/update/", {{ cookiecutter.app_name.title() }}UpdateView.as_view(), name="{{ cookiecutter.app_name }}_update"),
    path("<int:pk>/delete/", {{ cookiecutter.app_name.title() }}DeleteView.as_view(), name="{{ cookiecutter.app_name }}_delete"),
]
