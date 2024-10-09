import logging
from typing import Any

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import (
    Project,
    Brand,
    Device,
    Network,
    InstructionFile,
    File,
    Settings
)

logger = logging.getLogger(__name__)


class ProjectListView(ListView):
    """
    The "ProjectListView" class displays a list of projects
    """
    model = Project
    template_name = 'product/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:

        context = super().get_context_data(**kwargs)
        context.update(title='Network technologies')
        logger.info(f"`{self.request.user}` Рендеринг шаблона с проектами")
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'product/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(title=f'Detail info {self.model.project}')
        logger.info(f"`{self.request.user}` Рендеринг шаблона с детальной информацией ")
        return context