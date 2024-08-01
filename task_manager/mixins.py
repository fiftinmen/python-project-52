from django.conf import settings
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.contrib.messages import error


class PermissionScenarioMixin:
    """perms - dictionary with permissions specific for permission class#
    perms must be included into permission_required, permission_tests,
    permission_denied_action, permission_denied_messages during
    permission class initialization (__init__)
    perms dictionary keys - names of permissions,
    which are needed to access to model

    perms values include parameters needed to perform permission test:
        test - str name of permission class test method
        action - str name of permission class action method
        message - str value, showed by action if test is failed"""

    permissions_required = [None]
    permission_scenarios = {
        None: {"test": None, "action": None, "message": None}
    }

    def dispatch(self, request, *args, **kwargs):
        for perm in self.permissions_required:
            if perm is None:
                continue
            is_user_passes_test = getattr(
                self, self.permission_scenarios[perm]["test"]
            )(request, perm, *args, **kwargs)

            if not is_user_passes_test:
                action = getattr(
                    self, self.permission_scenarios[perm]["action"]
                )
                return action(request, perm, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

    def get_message(self, perm):
        return self.permission_scenarios[perm]["message"]


PERMISSION_SCENARIOS = {
    "login_required": {
        "login_required": {
            "test": "is_user_authenticated",
            "action": "redirect_to_login",
            "message": _("login_required"),
        }
    },
    "access_all": {
        "access_all": {
            "test": "is_user_permitted",
            "action": "redirect_to_next_page",
            "message": _("Not_permitted"),
        }
    },
}


class LoginRequiredScenarioMixin(PermissionScenarioMixin):

    login_url = None
    permissions_required = ["login_required"]
    permission_scenarios = PERMISSION_SCENARIOS["login_required"]

    def get_login_url(self):
        return self.login_url or settings.LOGIN_URL

    def is_user_authenticated(self, request, perm, *args, **kwargs):
        return request.user.is_authenticated

    def redirect_to_login(self, request, perm, *args, **kwargs):
        message = self.get_message(perm)
        error(request, message)
        return redirect(self.get_login_url(), *args, **kwargs)


class NotOwnObjectPermissionMixin(LoginRequiredScenarioMixin):

    permissions_required = ["login_required", "access_all"]
    permission_scenarios = (
        PERMISSION_SCENARIOS["login_required"]
        | PERMISSION_SCENARIOS["access_all"]
    )

    def is_user_object_owner(self, request):
        obj = self.model.objects.get(pk=self.kwargs["pk"])
        return request.user.pk == getattr(obj, self.owner_field).pk

    def is_user_permitted(self, request, perm, *args, **kwargs):
        return self.is_user_object_owner(request) or request.user.has_perm(perm)

    def redirect_to_next_page(self, request, perm, *args, **kwargs):
        message = self.get_message(perm)
        error(request, message)
        return redirect(self.next_page)
