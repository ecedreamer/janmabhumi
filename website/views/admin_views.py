import logging

from django.views import generic
from django.contrib.messages.views import messages
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
from website.forms import admin_forms
from website.models import Operator


logger = logging.getLogger("django")


class AdminLoginView(generic.FormView):
    template_name = "admintemplates/adminlogin.html"
    form_class = admin_forms.OperatorLoginForm
    success_url = reverse_lazy("website:admindashboard")

    def form_valid(self, form):
        operator = Operator.objects.get(user__username=form.cleaned_data.get("email"))
        login(self.request, operator.user)
        messages.success(self.request, "Admin logged in successfully...")

        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            return self.request.GET.get("next")
        return super().get_success_url()


class AdminRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        try:
            self.operator = request.user.operator
        except Exception:
            messages.error(request, "You have to login to do this operation")
            return redirect(reverse("website:adminlogin") + f"?next={request.path}")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operator"] = self.operator
        return context


class AdminLogoutView(AdminRequiredMixin, generic.View):
    def get(self, request):
        logout(request)
        return redirect("website:adminlogin")

class AdminDashboardView(AdminRequiredMixin, generic.TemplateView):
    template_name = "admintemplates/admindashboard.html"


class AdminPageCreateView(AdminRequiredMixin, generic.CreateView):
    template_name = "admintemplates/adminpagecreate.html"
    form_class = admin_forms.AdminPageForm
    success_url = "/admin"


class AdminPlaceCreateView(AdminRequiredMixin, generic.CreateView):
    template_name = "admintemplates/adminplacecreate.html"
    form_class = admin_forms.AdminPlaceForm
    success_url = "/admin"