from django.urls import path
from .views import (
    ProjectListView,
    ProjectDetailView,
    DeviceDetailView,
    SearchProjectView,
    InstructionFileView,
    CreateDeviceView
    )

app_name = 'project'

urlpatterns = [
    path('', ProjectListView.as_view(), name='index'),
    path('product/<slug:slug>/detail', ProjectDetailView.as_view(), name='product-detail'),
    path('product/<slug:slug>/create', CreateDeviceView.as_view(), name='device-create'),
    path('device/<slug:slug>/detail', DeviceDetailView.as_view(), name='device-detail'),
    path('product/search', SearchProjectView.as_view(), name='search'),
    path('documents/instructions', InstructionFileView.as_view(), name='instructions'),
    # path('brand', BrandView.as_view(), name='brand-list'),
    # path('brand/<slug:slug>', BrandDetailView.as_view(), name='brand-detail'),
    # path('documents/instructions/add', AddedInstructionView.as_view(), name='instruction-add'),
]
