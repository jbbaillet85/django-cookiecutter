from django.contrib import admin
from models import {{ cookiecutter.app_name }}

# Register your models here.
class {{ cookiecutter.app_name }}Admin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ["name"]


admin.site.register({{ cookiecutter.app_name }}, {{ cookiecutter.app_name }}Admin)