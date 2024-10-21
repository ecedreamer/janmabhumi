from django.views.generic import TemplateView
from website.views import client_views


class StatusCodeMixin:

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        response.status_code = self.status_code
        return response


class CustomBadRequestView(StatusCodeMixin, client_views.ClientMixin, TemplateView):
    template_name = "400.html"
    status_code = 400



class CustomPermissionDeniedView(StatusCodeMixin, client_views.ClientMixin, TemplateView):
    template_name = "403.html"
    status_code = 403


class CustomPageNotFoundView(StatusCodeMixin, client_views.ClientMixin, TemplateView):
    template_name = "404.html"
    status_code = 404


class CustomServerErrorView(StatusCodeMixin, client_views.ClientMixin, TemplateView):
    template_name = "500.html"
    status_code = 500
