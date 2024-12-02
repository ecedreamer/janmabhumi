import logging

from django.views import generic
from django.urls import reverse_lazy

from website.models import *
from website.forms.client_forms import *


class ClientMixin(object):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["site_info"] = SiteInfo.objects.filter(is_active=True).order_by("version").last()
        context["place_categories"] = PlaceCategory.objects.filter(is_active=True)
        return context


class HomeView(ClientMixin, generic.TemplateView):
    template_name = "clienttemplates/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["image_sliders"] = ImageSlider.objects.filter(is_active=True).order_by("-id")
        context["important_contants"] = ImportantContact.objects.filter(is_active=True).order_by("display_order")
        return context


class CulturesView(ClientMixin, generic.TemplateView):
    template_name = "clienttemplates/cultures.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cultural_groups"] = CulturalGroup.objects.filter(is_active=True,
                                                                  culturalevent__is_active=True).order_by("group_name")
        return context


class CulturalEventDetailView(ClientMixin, generic.DetailView):
    template_name = "clienttemplates/culturaleventdetail.html"
    model = CulturalEvent
    context_object_name = "culturalevent"


class AboutView(ClientMixin, generic.TemplateView):
    template_name = "clienttemplates/about.html"


class ContactView(ClientMixin, generic.CreateView):
    template_name = "clienttemplates/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("website:home")


class PageDetailView(ClientMixin, generic.DetailView):
    template_name = "clienttemplates/pagedetail.html"
    context_object_name = "page"

    def get_object(self, queryset=None):
        return ExtraPage.objects.filter(page_slug=self.kwargs["slug"]).first()


class PlaceListView(ClientMixin, generic.TemplateView):
    template_name = "clienttemplates/placelist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if "category" in self.kwargs:
                category = self.kwargs["category"]
                print(category, "--------------")
                context["category"] = PlaceCategory.objects.get(slug__iexact=category)
                places = Place.objects.filter(is_active=True, category__name__iexact=category).order_by("view_count")
            else:
                context["place_type"] = "popular_places"
                places = Place.objects.filter(is_active=True).order_by("view_count")
            context["placelist"] = places
            return context
        except Exception as e:
            logging.error(f"Invalid Category; {e}")
            context["error"] = "Invalid Category"
        return context


class PlaceDetailView(ClientMixin, generic.DetailView):
    template_name = "clienttemplates/placedetail.html"
    model = Place
    context_object_name = "place"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["executive_members"] = ExecutiveMembers.objects.filter(place_id=self.object).order_by("level")
        return context

    def get_object(self, queryset=None):
        place = super().get_object()
        place.view_count += 1
        place.save()
        return place
