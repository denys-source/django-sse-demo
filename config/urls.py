from django.contrib import admin
from django.urls import path, include

import django_eventstream

urlpatterns = [
    path("admin/", admin.site.urls),
    path("events/", include(django_eventstream.urls), {"channels": ["test"]}),
    path("", include("app.urls")),
]
