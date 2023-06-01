from models import {{ cookiecutter.app_name }}
from forms import {{ cookiecutter.app_name }}Form
from django.views.generic import CreateView


class BookCreateView(CreateView):
    model = {{ cookiecutter.app_name }}
    template_name = "{{ cookiecutter.app_name }}/add_book.html"
    form_class = {{ cookiecutter.app_name }}Form
