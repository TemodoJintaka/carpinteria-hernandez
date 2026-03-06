from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms
from django.core.exceptions import ValidationError
from django.forms import CharField
from django.forms import EmailField
from django.forms import ModelForm
from django.forms import PasswordInput
from django.utils.translation import gettext_lazy as _

from .models import User


class UserCreationForm(ModelForm):
    """Formulario para crear usuarios (staff)."""

    password1 = CharField(
        label=_("Password"),
        widget=PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = CharField(
        label=_("Password confirmation"),
        widget=PasswordInput(attrs={"autocomplete": "new-password"}),
    )

    class Meta:
        model = User
        fields = ("email", "name", "image")
        field_classes = {"email": EmailField}

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(_("The two password fields didn't match."))
        return password2

    def save(self, commit=True):
        extra = {"name": self.cleaned_data.get("name", "")}
        if self.cleaned_data.get("image"):
            extra["image"] = self.cleaned_data["image"]
        user = User.objects.create_user(
            email=self.cleaned_data["email"],
            password=self.cleaned_data["password1"],
            **extra,
        )
        return user


class UserUpdateForm(ModelForm):
    """Formulario para actualizar perfil: name, image y contraseña opcional."""

    email = EmailField(
        label=_("Email"),
        disabled=True,
        required=False,
    )
    password1 = CharField(
        label=_("Nueva contraseña"),
        widget=PasswordInput(attrs={"autocomplete": "new-password"}),
        required=False,
        help_text=_("Dejar en blanco para mantener la contraseña actual."),
    )
    password2 = CharField(
        label=_("Confirmar nueva contraseña"),
        widget=PasswordInput(attrs={"autocomplete": "new-password"}),
        required=False,
    )

    class Meta:
        model = User
        fields = ("email", "name", "image")
        field_classes = {"email": EmailField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields["email"].initial = self.instance.email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 or password2:
            if password1 != password2:
                raise ValidationError(_("Las dos contraseñas no coinciden."))
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password1")
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):  # type: ignore[name-defined]
        model = User
        field_classes = {"email": EmailField}


class UserAdminCreationForm(admin_forms.AdminUserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):  # type: ignore[name-defined]
        model = User
        fields = ("email",)
        field_classes = {"email": EmailField}
        error_messages = {
            "email": {"unique": _("This email has already been taken.")},
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """
