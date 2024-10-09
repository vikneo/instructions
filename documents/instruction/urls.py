from django.urls import path
from .views import (
    ProjectListView,
    ProjectDetailView
    )

app_name = 'project'

urlpatterns = [
    path('', ProjectListView.as_view(), name='index'),
    path('detail/<slug:slug>', ProjectDetailView.as_view(), name='product-detail')
]