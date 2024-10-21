from django.views import generic

class ClientMixin(object):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class HomeView(ClientMixin, generic.TemplateView):
    template_name = "clienttemplates/home.html"