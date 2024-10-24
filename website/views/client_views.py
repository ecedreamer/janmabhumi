from django.views import generic

from website.models import Page, PlaceCategory, Place


class ClientMixin(object):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["place_categories"] = PlaceCategory.objects.filter(is_active=True)
        return context


class HomeView(ClientMixin, generic.TemplateView):
    template_name = "clienttemplates/home.html"


class AboutView(ClientMixin, generic.TemplateView):
    template_name = "clienttemplates/about.html"


class ContactView(ClientMixin, generic.TemplateView):
    template_name = "clienttemplates/contact.html"


class PageDetailView(ClientMixin, generic.DetailView):
    template_name = "clienttemplates/pagedetail.html"
    context_object_name = "page"

    def get_object(self, queryset=None):
        return Page.objects.filter(page_slug=self.kwargs["slug"]).first()


class PlaceListView(ClientMixin, generic.ListView):
    template_name = "clienttemplates/placelist.html"
    context_object_name = "placelist"

    def get_queryset(self):
        print(self.request.GET)
        if "category" in self.kwargs:
            category = self.kwargs["category"]
            places = Place.objects.filter(is_active=True, category__name__iexact=category).order_by("view_count")
        else:
            places = Place.objects.filter(is_active=True).order_by("view_count")
        return places
