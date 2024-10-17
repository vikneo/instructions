import logging
from typing import Any

from django.core.exceptions import ValidationError
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
            f"`{format_name(self.request)}` - Рендеринг шаблона с Projects"
        )
        return context

    def get_queryset(self):
        if not cache.get("products"):
            logger.warning(f'Отсутствует кэш для Projects')
            logger.info(f'Сформирован кэш для Projects')

        products = cache.get_or_set('products', Project.objects.filter(archive=False))
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
            f"`{format_name(self.request)}` - Загружена страница с детальной информацией о {project}"
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
            logger.warning(f"'{format_name(self.request)}` - По данному запросу ничего не найдено")
            logger.exception(err)
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
                # messages.info(self.request, not_found)
                raise ValidationError(not_found)

            logger.info(f"'{format_name(self.request)}` - Выполнен запрос поиска с вводной `{self.request.GET.get('search')}`")

            return result
        except Exception as err:
            logger.warning(f"'{format_name(self.request)}` - {not_found}")
            logger.exception(err)
            # messages.info(self.request, not_found)


class InstructionFileView(ListView):
    """
    
    """
    template_name = 'documents/instruction.html'
    context_object_name = 'instructions'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            title='Инструкции'
        )
        logger.info(f"`{format_name(self.request)}` - Загружена страница {context['title']}")
        return context
    
    def get_queryset(self):
        if not cache.get('instructions'):
            logger.warning(f"Отсутствует кэш для Инструкций")
            logger.info(f"Сформирован кэш для Инструкций")
        
        instructions = cache.get_or_set("instructions", InstructionFile.objects.all())
        return instructions


class BrandView(ListView):
    """
    
    """
    template_name = 'brands/brand_list.html'
    context_object_name = 'brands'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            title='Производители',
        )

        logger.info(f"`{format_name(self.request)}` - Загружена страница {context['title']}")
        return context
    
    def get_queryset(self):
        if not cache.get('brands'):
            logger.warning(f"Отсутствует кэш для модели Brand")
            logger.info(f"Сформирован кэш для модели Brand")

        brands = cache.get_or_set('brands', Brand.objects.all())
        return brands


class BrandDetailView(DetailView):
    """
    
    """
    template_name = 'brands/brand_detail.html'
    context_object_name = 'brand'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            title=f"Brand -{self.model.objects.get(slug=self.kwargs['slug']).name}"
        )
        logger.info(f"{format_name(self.request)}` - Загружена страница {context['title']}")

        return context
    
    def get_queryset(self):
        brand = self.model.objects.get(slug=self.kwargs['slug']).name
        logger.info(f"`{format_name(self.request)}` - Загружена детальная информация о {brand}")
        return Brand.objects.get(slug=self.kwargs['slug'])
    
