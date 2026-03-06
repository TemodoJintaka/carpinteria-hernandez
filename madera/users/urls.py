from django.urls import path

from .views import user_create_view
from .views import user_delete_view
from .views import user_detail_view
from .views import user_list_view
from .views import user_redirect_view
from .views import user_staff_update_view
from .views import user_update_view

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("~delete/", view=user_delete_view, name="delete"),
    path("create/", view=user_create_view, name="create"),
    path("list/", view=user_list_view, name="list"),
    path("<int:pk>/edit/", view=user_staff_update_view, name="edit"),
    path("<int:pk>/", view=user_detail_view, name="detail"),
]
