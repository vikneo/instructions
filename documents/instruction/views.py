import logging
from typing import Any

from django.core.cache import cache
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
        logger.info(f"`{self.request.user}` - Рендеринг шаблона с проектами")
        return context
    
    def get_queryset(self):
        if not cache.get("products"):
            logger.info(f'Сформирован кэш для страницы с проектами')
        
        products = cache.get_or_set('products', Project.objects.all())
        return products


class ProjectDetailView(DetailView):
    """
    
    """
    model = Project
    template_name = 'product/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.model.objects.get(slug=self.kwargs['slug']).project
        context.update(title=f'{project} - Профиль')
        logger.info(f"`{self.request.user}` - Рендеринг шаблона с детальной информацией о {project}")
        return context


class DeviceDetailView(DetailView):
    """
    
    """
    model = Device
    template_name = 'device/device_detail.html'
    context_object_name = 'device'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        device = self.model.objects.get(slug=self.kwargs['slug'])
        context.update(
            title=f"{'device'} - Профиль"
        )
        logger.info(f"`{self.request.user}` - Получены данные о устройстве `{device.name}-{device.serial_num}`")
        return context
