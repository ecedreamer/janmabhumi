from django.urls import path
from .views import client_views, admin_views


app_name = "website"
urlpatterns = [
    ## client side views

    path("", client_views.HomeView.as_view(), name="home"),
    path("about/", client_views.AboutView.as_view(), name="about"),
    path("contact/", client_views.ContactView.as_view(), name="contact"),
    path("places/", client_views.PlaceListView.as_view(), name="placelist"),
    path("places/<slug>", client_views.PlaceDetailView.as_view(), name="placedetail"),
    path("<category>/places/", client_views.PlaceListView.as_view(), name="categorizedplacelist"),

    path("<slug>/", client_views.PageDetailView.as_view(), name="pagedetail"),  # dont put any url with single path param below this

    ## admin side views

    path("operator/login", admin_views.AdminLoginView.as_view(), name="adminlogin"),
    path("operator/dashboard", admin_views.AdminDashboardView.as_view(), name="admindashboard"),
    path("operator/pages/create", admin_views.AdminPageCreateView.as_view(), name="adminpagecreate"),
    path("operator/place/create", admin_views.AdminPlaceCreateView.as_view(), name="adminplacecreate"),
]