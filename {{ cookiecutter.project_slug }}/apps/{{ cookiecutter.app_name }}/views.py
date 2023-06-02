from models import {{ cookiecutter.app_name }}
from forms import {{ cookiecutter.app_name }}Form
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

class {{ cookiecutter.app_name }}CreateView(CreateView):
    model = {{ cookiecutter.app_name }}
    template_name = "{{ cookiecutter.app_name }}/create_{{ cookiecutter.app_name }}.html"
    form_class = {{ cookiecutter.app_name }}Form

class {{ cookiecutter.app_name }}UpdateView(UpdateView):
    model = {{ cookiecutter.app_name }}
    template_name = "{{ cookiecutter.app_name }}/update_{{ cookiecutter.app_name }}.html"
    form_class = {{ cookiecutter.app_name }}Form

class {{ cookiecutter.app_name }}DeleteView(DeleteView):
    model = {{ cookiecutter.app_name }}
    template_name = "{{ cookiecutter.app_name }}/delete_{{ cookiecutter.app_name }}.html"
    success_url = "/"  # Rediriger vers l'URL souhaitée après la suppression

class {{ cookiecutter.app_name }}DetailView(DetailView):
    model = {{ cookiecutter.app_name }}
    template_name = "{{ cookiecutter.app_name }}/detail_{{ cookiecutter.app_name }}.html"

class {{ cookiecutter.app_name }}ListView(ListView):
    model = {{ cookiecutter.app_name }}
    template_name = "{{ cookiecutter.app_name }}/list_{{ cookiecutter.app_name }}.html"

