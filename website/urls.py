from django.urls import path
from .views import client_views, admin_views


urlpatterns = [
    ## client side views

    path("", client_views.HomeView.as_view(), name="home"),

    ## admin side views

    path("operator/dashboard", admin_views.AdminDashboardView.as_view(), name="admindashboard"),
    path("operator/pages/create", admin_views.AdminPageCreateView.as_view(), name="adminpagecreate"),
]