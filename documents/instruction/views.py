import logging
from typing import Any

from django.db.models import Q
from django.http import Http404
from django.core.cache import cache
from django.views.generic import ListView, DetailView

from .models import (
    Project,
    Brand,
    Device,
    Network,
    InstructionFile,
    File,
    Settings,
)
from utils.format_name_uer import format_name

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
        context.update(title = 'Network technologies')
        logger.info(
            f"`{format_name(self.request)}` - Рендеринг шаблона с проектами"
        )
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
        project = self.model.objects.get(slug = self.kwargs['slug']).project
        context.update(title = f'{project} - Профиль')
        logger.info(
            f"`{format_name(self.request)}` - Рендеринг шаблона с детальной информацией о {project}"
        )
        return context


class DeviceDetailView(DetailView):
    """
    
    """
    model = Device
    template_name = 'device/device_detail.html'
    context_object_name = 'device'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        device = self.model.objects.get(slug = self.kwargs['slug'])
        context.update(
            title = f"{'device'} - Профиль"
        )
        logger.info(
            f"`{format_name(self.request)}` - Получены данные о устройстве `{device.name}-{device.serial_num}`"
        )
        return context


class SearchProjectView(ListView):
    """
    
    """
    template_name = 'product/search.html'
    context_object_name = 'searches'
    # paginate_by = settings.get_paginate_by()
    allow_empty = True

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
        except Exception as err:
            logger.warning(f"'{format_name(self.request)}` - Данный запрос не  существует")
            raise Http404("Poll does not exist")

        context.update(
            title = f"Результат поиска - {self.request.GET.get('search')}"
        )
        logger.info(f"'{format_name(self.request)}` - Рендеринг шаблона поискового запроса")
        return context

    def get_queryset(self):
        not_found = 'Нет ни одного совпадения'
        try:
            query = self.request.GET.get('search').upper()
            result = Project.objects.filter(
                Q(crm_id__icontains = query) |
                Q(project__icontains = query)
            )

            if not result:
                logger.info(f"'{format_name(self.request)}` - {not_found}")
                # messages.info(self.request, not_found)

            logger.info(f"'{format_name(self.request)}` - Выполнен запрос поиска с вводной `{self.request.GET.get('search')}`")

            return result
        except Exception as err:
            logger.warning(f"'{format_name(self.request)}` - {not_found} [{err}]")
            # messages.info(self.request, not_found)
