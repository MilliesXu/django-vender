from django.urls import path

from .views import (
    MaterialListView,
    MaterialCreateView,
    MaterialDeleteView,
    MaterialUpdateView,
    MaterialDetailView
)

urlpatterns = [
    path('', MaterialListView.as_view(), name='materials'),
    path('create/', MaterialCreateView.as_view(), name='materials-create'),
    path(
        '<int:pk>/detail',
        MaterialDetailView.as_view(),
        name='materials-detail'
    ),
    path(
        '<int:pk>/update',
        MaterialUpdateView.as_view(),
        name='materials-update'
    ),
    path(
        '<int:pk>/delete',
        MaterialDeleteView.as_view(),
        name='materials-delete'
    )
]
