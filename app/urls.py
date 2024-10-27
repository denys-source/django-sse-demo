from django.urls import path

from . import views


urlpatterns = [
    path("clock/", views.clock, name="clock"),
    path("send-event/", views.send_event_view, name="send_event"),
]
