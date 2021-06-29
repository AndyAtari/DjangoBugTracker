from django.urls import path
from welcome import views 

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("tracker/", views.tracker, name="tracker"),
]
