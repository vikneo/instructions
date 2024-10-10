import logging

from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView


logger = logging.getLogger(__name__)


class LoginUserView(LoginView):
    """
    Authorization user view.
    """
    template_name = 'account/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            title='Авторизация'
        )
        logger.info("Загружена страница '%s'", context['title'])
        return context

    def get_success_url(self):
        return reverse_lazy('project:index')


class LogoutUserView(LogoutView):
    """
    Logout user view.
    """
    next_page = reverse_lazy('project:index')

    def dispatch(self, request, *args, **kwargs):
        logger.info("User '%s' logged out", request.user)
        return super().post(request, *args, **kwargs)
