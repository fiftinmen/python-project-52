import django_filters
from django.forms import CheckboxInput
from django.utils.translation import gettext_lazy as _
from .models import Task
from task_manager.mixins import NoColonsFilterMixin


class TasksFilter(NoColonsFilterMixin, django_filters.FilterSet):
    labels = django_filters.ChoiceFilter(label=_("Label"))
    only_own_tasks = django_filters.BooleanFilter(
        label=_("Only own tasks"), widget=CheckboxInput, method="get_own_tasks"
    )

    def get_own_tasks(self, queryset, name, value):
        return queryset.filter(author=self.request.user) if value else queryset

    class Meta:
        model = Task
        fields = ("status", "executor", "labels", "only_own_tasks")
