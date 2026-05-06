from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import QuerySet
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import RedirectView
from django.views.generic import UpdateView

from madera.users.forms import UserCreationForm
from madera.users.forms import UserUpdateForm
from madera.users.models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_message = _("Information successfully updated")

    def get_success_url(self) -> str:
        assert self.request.user.is_authenticated  # type guard
        return self.request.user.get_absolute_url()

    def get_object(self, queryset: QuerySet | None = None) -> User:
        assert self.request.user.is_authenticated  # type guard
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserStaffUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = User
    form_class = UserUpdateForm
    template_name = "users/user_form.html"
    success_message = _("Information successfully updated")

    def test_func(self) -> bool:
        return self.request.user.is_staff

    def get_success_url(self) -> str:
        return reverse("users:detail", kwargs={"pk": self.object.pk})


user_staff_update_view = UserStaffUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self) -> str:
        return reverse("users:detail", kwargs={"pk": self.request.user.pk})


user_redirect_view = UserRedirectView.as_view()


class UserCreateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    CreateView,
):
    model = User
    form_class = UserCreationForm
    template_name = "users/user_form_create.html"
    success_message = _("User created successfully")

    def test_func(self) -> bool:
        return self.request.user.is_staff

    def get_success_url(self) -> str:
        return reverse("users:detail", kwargs={"pk": self.object.pk})


user_create_view = UserCreateView.as_view()


class UserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = "users/user_list.html"
    context_object_name = "user_list"

    def test_func(self) -> bool:
        return self.request.user.is_staff


user_list_view = UserListView.as_view()


class UserDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = "users/user_confirm_delete.html"
    success_message = _("Account successfully deleted")

    def get_success_url(self) -> str:
        return reverse("home")

    def get_object(self, queryset: QuerySet | None = None) -> User:
        return self.request.user


user_delete_view = UserDeleteView.as_view()
