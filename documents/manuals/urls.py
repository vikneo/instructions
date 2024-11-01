from django.urls import path

from .views import (
    BrandView
)

app_name = 'manual'

urlpatterns = [
    path("", BrandView.as_view(), name='brand-list'),
]