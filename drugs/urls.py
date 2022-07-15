from django.urls import path

from drugs.views import home

urlpatterns = [
    path('', home),
]
