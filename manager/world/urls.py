from django.urls import path

from . import views

urlpatterns = [
    path("", views.RegionsListView.as_view(), name="regions-list"),
    path(
        "create-region",
        views.RegionsCreateView.as_view(),
        name="regions-creation",
    ),
]
