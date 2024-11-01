from django.urls import path

from .views import (
    BrandView,
    BrandDetailView
)

app_name = 'manual'

urlpatterns = [
    path("", BrandView.as_view(), name='brand-list'),
    path("detail/<slug:slug>", BrandDetailView.as_view(), name='brand-detail'),
]