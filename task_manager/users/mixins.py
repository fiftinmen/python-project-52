from django.utils.translation import gettext_lazy as _
from task_manager.mixins import (
    NotOwnObjectPermissionMixin,
    PERMISSION_SCENARIOS,
)


class UsersModifyPermissionMixin(NotOwnObjectPermissionMixin):

    permissions_required = ["login_required", "users.modify_all"]
    permission_scenarios = PERMISSION_SCENARIOS["login_required"] | {
        "users.modify_all": {
            "test": "is_user_permitted",
            "action": "redirect_to_next_page",
            "message": _("You not permitted to modify other user"),
        }
    }

    def is_user_object_owner(self, request):
        return request.user.pk == self.kwargs["pk"]
