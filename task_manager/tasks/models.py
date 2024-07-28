from django.db import models
from task_manager.statuses.models import Status
from task_manager.users.models import CustomUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Task(models.Model):
    name = models.CharField(
        max_length=100, default="name", unique=True, verbose_name=_("Name")
    )
    description = models.TextField(
        max_length=2048, blank=True, verbose_name=_("Description")
    )
    created_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Created_at")
    )
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT, verbose_name=_("Status")
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        related_name="task_author",
        verbose_name=_("Author"),
    )
    executor = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        related_name="task_executor",
        blank=True,
        null=True,
        verbose_name=_("Executor"),
    )
    labels = models.ManyToManyField(
        to="labels.Label",
        through="TaskLabels",
        blank=True,
        verbose_name=_("Labels"),
    )

    REQUIRED_FIELDS = ["name", "status", "author"]

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")
        permissions = [
            ("tasks.delete_all", "Can delete all tasks"),
            ("tasks.delete_own", "Can delete own tasks"),
        ]

    def __str__(self):
        return self.name


class TaskLabels(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(to="labels.Label", on_delete=models.PROTECT)
