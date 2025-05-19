import logging
from itertools import chain
from typing import Any, Dict

from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from manuals.models import Module
from utils.format_name_uer import format_name

from .forms import AddFileForm, CreatedDeviceForm, CrerateprojectForm
from .models import Device, FileProject, Project

logger = logging.getLogger(__name__)


class ProjectListView(ListView):
    """
    The "ProjectListView" class displays a list of projects
    """

    model = Project
    template_name = "product/product_list.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs: dict) -> Dict[str, Any]:
        context: dict = super().get_context_data(**kwargs)
        context.update(title="Network technologies")
        logger.info(f"`{format_name(self.request)}` - Рендеринг шаблона с Projects")
        return context

    def get_queryset(self):
        if not cache.get("products"):
            logger.warning("Отсутствует кэш для Projects")
            logger.info("Сформирован кэш для Projects")

        products = cache.get_or_set(
            "products", Project.objects.filter(archive=False).order_by("-created_at")
        )
        return products


class ProjectDetailView(DetailView):
    """ """

    model = Project
    template_name = "product/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.model.objects.get(slug=self.kwargs["slug"]).project
        context.update(title=f"{project} - Профиль")
        logger.info(
            f"`{format_name(self.request)}` - Загружена страница с детальной информацией о {project}"
        )
        return context


class ProjectCreateView(CreateView):
    """ """

    template_name = "product/project_create.html"
    form_class = CrerateprojectForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(title="Добавление проекта")
        logger.info("Рендеринг шаблона с формой добавления проекта")
        return context

    def form_valid(self, form):
        form.save()
        logger.info("Сохранена форма с добавлением проекта")
        return super().form_valid(form)


class AddFileProjectView(CreateView):
    """ """

    template_name = "product/file_upload.html"
    form_class = AddFileForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Project.objects.get(slug=self.kwargs["slug"])
        context.update(title=f"Добавить файлы к проекту {product}", product=product)
        return context

    def form_valid(self, form):
        files = self.request.FILES.getlist("file")
        product = self.get_context_data().get("product")
        if not files:
            return self.form_invalid(form)

        for file in files:
            FileProject.objects.create(project_id=product, name=str(file), file=file)
        logger.info(f"Добавлены файлы к проекту - {product}")
        product.save()  # type: ignore
        logger.info(f"Сохранен проект - {product}. Для отчистки кэша")
        return HttpResponseRedirect(
            reverse_lazy("project:product-detail", kwargs={"slug": self.kwargs["slug"]})
        )


class IdCRMDetailView(ListView):
    """ """
    model = Project
    template_name = "product/product_crm.html"
    context_object_name = "crm_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self.model.objects.filter(crm_id=self.kwargs["crm_id"])
        title = f"ID-{str(products[0]).split('-')[0]}"
        context.update(title=title, current_path=self.request.META.get("HTTP_REFERER"))
        logger.info(
            f"`{format_name(self.request)}` - Получена детальная информация о `{title}`"
        )
        return context

    def get_queryset(self):
        products = Project.objects.filter(crm_id=self.kwargs["crm_id"])
        logger.info(
            f"`{format_name(self.request)}` - Получены проекты в кол-ве {len(products)} шт."
        )
        return products


class DeviceDetailView(DetailView):
    """ """

    model = Device
    template_name = "device/device_detail.html"
    context_object_name = "device"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        device = self.model.objects.get(slug=self.kwargs["slug"])
        context.update(title=f"{'device'} - Профиль")
        logger.info(
            f"`{format_name(self.request)}` - Получены данные о устройстве` "
            f"{device.name}-{device.serial_num}`"
        )
        return context


class SearchProjectView(ListView):
    """ """

    template_name = "product/search.html"
    context_object_name = "searches"
    # paginate_by = settings.get_paginate_by()
    allow_empty = True

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
        except Exception as err:
            logger.warning(
                f"'{format_name(self.request)}` - По данному запросу ничего не найдено"
            )
            logger.exception(err)
            raise Http404("Poll does not exist")

        context.update(title=f"Результат поиска - {self.request.GET.get('search')}")
        logger.info(
            f"'{format_name(self.request)}` - Рендеринг шаблона поискового запроса"
        )
        return context

    def get_queryset(self):  # type: ignore
        not_found = "Нет ни одного совпадения"
        try:
            query = self.request.GET.get("search").upper()
            product = Project.objects.filter(
                Q(crm_id__icontains=query) | Q(project__icontains=query)
            )
            instruct = Module.objects.filter(Q(name__icontains=query))
            result = list(chain(product, instruct))
            try:
                if product[0].project.lower() == "no name":
                    raise ValidationError(not_found)
            except IndexError as err:
                logger.exception(err)

            if not result:
                logger.info(
                    f"'{format_name(self.request)}` - Результат поиска ...", not_found
                )
                raise ValidationError(not_found)

            logger.info(
                f"'{format_name(self.request)}` - Выполнен запрос поиска с вводной` "
                f"{self.request.GET.get('search')}`"
            )

            return result
        except Exception as err:
            logger.warning(f"'{format_name(self.request)}` - {not_found}")
            logger.exception(err)
            # messages.info(self.request, not_found)


class InstructionFileView(ListView):
    """ """

    template_name = "documents/instruction.html"
    context_object_name = "instructions"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(title="Инструкции")
        logger.info(
            f"`{format_name(self.request)}` - Загружена страница {context['title']}"
        )
        return context

    def get_queryset(self):
        if not cache.get("instructions"):
            logger.warning("Отсутствует кэш для Инструкций")
            logger.info("Сформирован кэш для Инструкций")

        instructions = cache.get_or_set("instructions", Module.objects.all())
        return instructions


# class BrandView(ListView):
#     """

#     """
#     template_name = 'brands/brand_list.html'
#     context_object_name = 'brands'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update(
#             title="Производители",
#         )

#         logger.info(f"`{format_name(self.request)}` - Загружена страница {context['title']}")
#         return context

#     def get_queryset(self):
#         if not cache.get('brands'):
#             logger.warning(f"Отсутствует кэш для модели Brand")
#             logger.info(f"Сформирован кэш для модели Brand")

#         brands = cache.get_or_set('brands', Brand.objects.all())
#         return brands


# class BrandDetailView(DetailView):
#     """

#     """
#     template_name = 'brands/brand_detail.html'
#     context_object_name = 'brand'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update(
#             title=f"Brand -{self.model.objects.get(slug=self.kwargs['slug']).name}"
#         )
#         logger.info(f"{format_name(self.request)}` - Загружена страница {context['title']}")

#         return context

#     def get_queryset(self):
#         brand = self.model.objects.get(slug=self.kwargs['slug']).name
#         logger.info(f"`{format_name(self.request)}` - Загружена детальная информация о {brand}")
#         return Brand.objects.get(slug=self.kwargs['slug'])


# class AddedInstructionView(CreateView):
#     """

#     """
#     model = Instructions
#     template_name = 'documents/add_instruction.html'
#     form_class = CreatedInstructionForms

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update(
#             title='Добавить инструкцию'
#         )
#         logger.info(f"Загружен шаблон с добавлением инструкции")
#         return context

#     def form_valid(self, form):
#         form.save()
#         logger.info(f"`{format_name(self.request)}` - Добавил инструкцию для "
#                     f"{self.request.POST.get('name')}")
#         return super().form_valid(form)

#     def get_absolute_url(self):
#         return reverse_lazy('project:instructions')


class CreateDeviceView(CreateView):
    """ """

    model = Device
    form_class = CreatedDeviceForm
    template_name = "device/create_device.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(title="Добавить устройство", slug=self.kwargs["slug"])
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_absolute_url(self):
        return reverse_lazy("project:product-detail", slug=self.kwargs["slug"])
