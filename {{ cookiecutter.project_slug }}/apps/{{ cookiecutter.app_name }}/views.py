from apps.{{ cookicutter.app_name }}.models import {{ cookiecutter.app_name.title() }}
from apps.{{ cookicutter.app_name }}.forms import {{ cookiecutter.app_name.title() }}Form
from django.views.generic import (CreateView, UpdateView,
                                  DeleteView, DetailView, ListView)

class {{ cookiecutter.app_name.title() }}CreateView(CreateView):
    model = {{ cookiecutter.app_name.title() }}
    template_name = "{{ cookiecutter.app_name }}/create_{{ cookiecutter.app_name }}.html"
    form_class = {{ cookiecutter.app_name.title() }}Form


class {{ cookiecutter.app_name.title }}UpdateView(UpdateView):
    model = {{ cookiecutter.app_name.title() }}
    template_name = "{{ cookiecutter.app_name }}/update_{{ cookiecutter.app_name }}.html"
    form_class = {{ cookiecutter.app_name.title() }}Form


class {{ cookiecutter.app_name.title() }}DeleteView(DeleteView):
    model = {{ cookiecutter.app_name.title() }}
    template_name = "{{ cookiecutter.app_name }}/delete_{{ cookiecutter.app_name }}.html"
    success_url = "/"  # Rediriger vers l'URL souhaitée après la suppression


class {{ cookiecutter.app_name.title }}DetailView(DetailView):
    model = {{ cookiecutter.app_name.title }}
    template_name = "{{ cookiecutter.app_name }}/detail_{{ cookiecutter.app_name }}.html"


class {{ cookiecutter.app_name.title() }}ListView(ListView):
    model = {{ cookiecutter.app_name.title() }}
    template_name = "{{ cookiecutter.app_name }}/list_{{ cookiecutter.app_name }}.html"
