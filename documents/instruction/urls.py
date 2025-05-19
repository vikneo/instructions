from django.urls import path

from .views import (
    AddFileProjectView,
    CreateDeviceView,
    DeviceDetailView,
    IdCRMDetailView,
    InstructionFileView,
    ProjectCreateView,
    ProjectDetailView,
    ProjectListView,
    SearchProjectView,
)

app_name = "project"

urlpatterns = [
    path("", ProjectListView.as_view(), name="index"),
    path(
        "product/<slug:slug>/detail", ProjectDetailView.as_view(), name="product-detail"
    ),
    path("product/create", ProjectCreateView.as_view(), name="product-create"),
    path(
        "product/<slug:slug>/add_files", AddFileProjectView.as_view(), name="add-files"
    ),
    path("id_crm/<int:crm_id>/detail", IdCRMDetailView.as_view(), name="id_crm-detail"),
    path(
        "product/<slug:slug>/create", CreateDeviceView.as_view(), name="device-create"
    ),
    path("device/<slug:slug>/detail", DeviceDetailView.as_view(), name="device-detail"),
    path("product/search", SearchProjectView.as_view(), name="search"),
    path("documents/instructions", InstructionFileView.as_view(), name="instructions"),
    # path('brand', BrandView.as_view(), name='brand-list'),
    # path('brand/<slug:slug>', BrandDetailView.as_view(), name='brand-detail'),
    # path('documents/instructions/add', AddedInstructionView.as_view(), name='instruction-add'),
]
