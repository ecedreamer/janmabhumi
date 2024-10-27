from django.contrib import admin
from django.apps import apps
from django.contrib.admin import site
from django_summernote.admin import SummernoteModelAdmin
from .models import Place


class PlaceAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

    class Media:
        css = {
            'all': ('/static/adminstatic/custom_admin.css',)  # Replace with the path to your custom CSS
        }

admin.site.register(Place, PlaceAdmin)


def register_models():
    models = set()
    for app in apps.get_app_configs():
        for model in app.get_models():
            if model._meta.app_label in ['admin', "django_summernote"] or model in site._registry:
                continue
            models.add(model)
    admin.site.register(models)


register_models()
