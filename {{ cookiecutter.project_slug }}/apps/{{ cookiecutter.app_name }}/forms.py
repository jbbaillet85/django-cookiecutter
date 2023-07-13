from models import {{ cookiecutter.app_name.title() }}
from django import forms


class {{ cookiecutter.app_name }}Form(forms.ModelForm):

    class Meta:
        model = {{ cookiecutter.app_name.title() }}
        fields = [
            'name',
        ]
        help_texts = {
            'name': 'Le nom de {{ cookiecutter.app_name }}',
        }
