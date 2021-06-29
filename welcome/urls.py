from django.urls import path
from welcome import views 

urlpatterns = [
    path("", views.home, name="home"),
    path("welcome/<name>", views.welcome_there, name="welcome_there"),
    path("about/", views.about, name="about"),
    path("tracker/", views.tracker, name="tracker"),
]
