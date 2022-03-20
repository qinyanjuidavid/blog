from django.urls import path
from polls import views

urlpattern = [
    path("info/", views.info, name="info")

]