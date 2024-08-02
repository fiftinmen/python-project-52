from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
)

from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, password_validation

from django import forms
from django.utils.translation import gettext_lazy as _


class UsersRegisterForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2",
        ]


class UsersUpdateForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "first_name",
            "last_name",
        ]

    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }
    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=_("Enter the same password as before, for verification."),
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        if password := self.cleaned_data.get("password2"):
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("password2", error)

    def save(self, commit=True):
        self.instance = super().save()
        password = self.cleaned_data["password1"]
        self.instance.set_password(password)
        if commit:
            self.instance.save()
        return self.instance
