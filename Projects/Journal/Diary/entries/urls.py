from django.urls import path

from . import views


urlpatterns = [
    # connects templates/entries to Django
    # path() function must have at least two arguments. 1. a route and reference to a view
    path(
        "", views.EntryListView.as_view(), name="entry-list"
    ),
    path(
        "entry/<int:pk>", views.EntryDetailView.as_view(), name="entry-detail"
    ),
    path(
        "create", views.EntryCreateView.as_view(), name="entry-create"
    ),
    # the entries above only require a basic create path

    # the entries below require a primary key to identify which  entry should be updated or deleted
    path(
        "entry/<int:pk>/update",  # <int:pk> == primary key
        views.EntryUpdateView.as_view(),
        name="entry-update",
    ),
    path(
        "entry/<int:pk>/delete",
        views.EntryDeleteView.as_view(),
        name="entry-delete",
    ),
]
