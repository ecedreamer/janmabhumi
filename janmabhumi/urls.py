from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .error_views import *

urlpatterns = [
    path('', include("website.urls", namespace="website")),
    path('dev/admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

handler400 = CustomBadRequestView.as_view()
handler403 = CustomPermissionDeniedView.as_view()
handler404 = CustomPageNotFoundView.as_view()
handler500 = CustomServerErrorView.as_view()
