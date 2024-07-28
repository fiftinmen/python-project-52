from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        verbose_name=_("Username"),
        unique=True,
        help_text=_(
            "Обязательное поле. Не более 150 символов. Только буквы, "
            "цифры и символы @/./+/-/_."
        ),
    )
    first_name = models.CharField(max_length=150, verbose_name=_("First name"))
    last_name = models.CharField(max_length=150, verbose_name=_("Last name"))
    password = models.CharField(verbose_name=_("Password"), max_length=128)
    date_joined = models.DateTimeField(
        verbose_name=_("date joined"), default=timezone.now
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["first_name", "last_name", "password"]

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        permissions = [
            ("users.update_all", "Can update all users"),
            ("users.delete_all", "Can delete all users"),
            ("users.update_self", "Can self update"),
            ("users.delete_self", "Can self delete"),
        ]

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.username
