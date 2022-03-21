from django.urls import path
from polls import views

urlpatterns = [
    path("info/", views.info, name="info")

]