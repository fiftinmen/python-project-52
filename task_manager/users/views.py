from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from . import forms
from .mixins import UsersModifyPermissionMixin


class UsersIndexView(ListView):
    model = get_user_model()
    pagination = 10
    template_name = "users/index.html"
    extra_context = {"page_header": _("Users")}


class UsersDetailView(DetailView):
    model = get_user_model()
    template_name = "users/detail.html"

    def get_object(self, queryset=None):
        if self.request.user.is_authenticated:
            return self.request.user
        return redirect("index")


class UsersCreateView(SuccessMessageMixin, CreateView):
    form_class = forms.UsersRegisterForm
    template_name = "users/create.html"
    next_page = reverse_lazy("index")
    success_url = reverse_lazy("login")
    success_message = _("Registration_success")


class UsersUpdateView(
    UsersModifyPermissionMixin, SuccessMessageMixin, UpdateView
):
    model = get_user_model()
    perms = ["users.update_all"]
    form_class = forms.UsersUpdateForm
    template_name = "users/update.html"
    next_page = success_url = reverse_lazy("users_index")
    success_message = _("User_update_success")


class UsersDeleteView(
    UsersModifyPermissionMixin, SuccessMessageMixin, DeleteView
):
    model = get_user_model()
    perms = ["users.delete_all"]
    template_name = "users/delete.html"
    next_page = success_url = reverse_lazy("users_index")
    success_message = _("User_deletion_success")
