
from django.contrib import admin
from django.urls import path
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('function.resident_function.urls')),
    path('',include('function.services_function.urls')),
    path('',include('function.dashboard_function.urls')),
    path('',include('function.complaints_function.urls')),
    path('',include('function.annoucement_function.urls')),
    path('',include('function.clearance_function.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
