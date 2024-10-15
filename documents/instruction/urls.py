from django.urls import path
from .views import (
    ProjectListView,
    ProjectDetailView,
    DeviceDetailView,
    SearchProjectView,
    )

app_name = 'project'

urlpatterns = [
    path('', ProjectListView.as_view(), name='index'),
    path('product/<slug:slug>/detail', ProjectDetailView.as_view(), name='product-detail'),
    path('device/<slug:slug>/detail', DeviceDetailView.as_view(), name='device-detail'),
    path('product/search', SearchProjectView.as_view(), name='search'),
]
