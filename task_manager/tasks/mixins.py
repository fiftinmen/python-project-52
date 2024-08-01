from task_manager.mixins import (
    NotOwnObjectPermissionMixin,
    PERMISSION_SCENARIOS,
)
from django.utils.translation import gettext_lazy as _


class TasksDeletePermissionMixin(NotOwnObjectPermissionMixin):

    permissions_required = ["login_required", "tasks.delete_all"]
    permission_scenarios = PERMISSION_SCENARIOS["login_required"] | {
        "tasks.delete_all": {
            "test": "is_user_permitted",
            "action": "redirect_to_next_page",
            "message": _("Only task's author can delete it"),
        }
    }
