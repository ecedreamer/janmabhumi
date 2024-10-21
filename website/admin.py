from django.contrib import admin
from django.apps import apps
from django.contrib.admin import site


def register_models():
    models = set()
    for app in apps.get_app_configs():
        for model in app.get_models():
            if model._meta.app_label in ['admin', "django_summernote"] or model in site._registry:
                continue
            models.add(model)
    admin.site.register(models)


register_models()
