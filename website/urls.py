from django.urls import path
from .views import client_views, admin_views


urlpatterns = [
    ## client side views

    path("", client_views.HomeView.as_view(), name="home"),
    path("about/", client_views.AboutView.as_view(), name="about"),

    path("<slug>/", client_views.PageDetailView.as_view(), name="pagedetail"), ## dont put any url with single path param below this

    ## admin side views

    path("operator/dashboard", admin_views.AdminDashboardView.as_view(), name="admindashboard"),
    path("operator/pages/create", admin_views.AdminPageCreateView.as_view(), name="adminpagecreate"),
]