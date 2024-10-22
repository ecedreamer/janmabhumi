from django.views import generic
from website.models import Page


class ClientMixin(object):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class HomeView(ClientMixin, generic.TemplateView):
    template_name = "clienttemplates/home.html"


class AboutView(ClientMixin, generic.TemplateView):
    template_name = "clienttemplates/about.html"


class PageDetailView(ClientMixin, generic.DetailView):
    template_name = "clienttemplates/pagedetail.html"
    context_object_name = "page"

    def get_object(self, queryset=None):
        return Page.objects.filter(page_slug=self.kwargs["slug"]).first()
