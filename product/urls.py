from django.urls import path
from .views import (
    ProductListView,
    ProductCreateView,
    ProductDetailView,
    ProductDeleteView,
    ProductUpdateView
)

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('create', ProductCreateView.as_view(), name='products-create'),
    path(
        '/<int:pk>/detail',
        ProductDetailView.as_view(),
        name='products-detail'
    ),
    path(
        '/<int:pk>/update',
        ProductUpdateView.as_view(),
        name='products-update'
    ),
    path(
        '/<int:pk>/delete',
        ProductDeleteView.as_view(),
        name='products-delete'
    ),
]
