import logging

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import AuthFormUser, RegisterFormUser

logger = logging.getLogger(__name__)


class RegisterUserView(CreateView):
    """ """

    form_class = RegisterFormUser
    template_name = "account/register.html"
    success_url = reverse_lazy("project:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(title="Регистрация")
        logger.info("Загружена страница `%s`", context["title"])
        return context


class LoginUserView(LoginView):
    """
    Authorization user view.
    """

    form_class = AuthFormUser
    template_name = "account/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(title="Авторизация")
        logger.info("Загружена страница `%s`", context["title"])
        return context

    def get_success_url(self):
        return reverse_lazy("project:index")


class LogoutUserView(LogoutView):
    """
    Logout user view.
    """

    next_page = reverse_lazy("project:index")

    def dispatch(self, request, *args, **kwargs):
        logger.info("User '%s' Вышел из системы", request.user)
        return super().post(request, *args, **kwargs)
