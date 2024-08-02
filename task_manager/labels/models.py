from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Label(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Name"))
    created_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Created_at")
    )
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Label")
        verbose_name_plural = _("Labels")


"""     def delete(self, *args, **kwargs):
        if self.tasks.exists():
            raise ValidationError(
                _(
                    "Cannot delete this label because it is associated with"
                    "one or more tasks."
                )
            )
        super().delete(*args, **kwargs)
 """
