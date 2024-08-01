from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.contrib.messages import info
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


@require_GET
def index(request):
    return render(request, "index.html")


class CustomLoginView(SuccessMessageMixin, LoginView):
    model = get_user_model()
    template_name = "login.html"
    next_page = success_url = reverse_lazy("index")
    success_message = _("Logged_in")


class CustomLogoutView(LogoutView):
    next_page = success_url = reverse_lazy("index")
    template_name = "index.html"

    def post(self, request, *args, **kwargs):
        info(request, _("Logged out"))
        return super().post(request, *args, **kwargs)
