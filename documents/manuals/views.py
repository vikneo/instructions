import logging

from django.core.cache import cache
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import (
    Brand,
    Module
)
from utils.format_name_uer import format_name

logger = logging.getLogger(__name__)


class BrandView(ListView):
    """
    The "BrandView" class displays a list of all manufacturers
    """
    model = Brand
    template_name = 'documents/brand_list.html'
    context_object_name = 'brands'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            title='Производители'
        )
        logger.info(f"`{format_name(self.request)}` - Загрузка шаблона с {context['title']}")
        return context
    
    def get_queryset(self):
        if not cache.get('brands'):
            logger.warning(f"Отсутствует кэш для модели Brand")

        brands = cache.get_or_set('brands', Brand.objects.all())
        logger.info(f"Сформирован кэш для модели Brand")
        return brands
