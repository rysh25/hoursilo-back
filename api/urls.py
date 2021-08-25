from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

app_name = "user"

router = DefaultRouter()

urlpatterns = [
    path("users/create/", views.CreateUserView.as_view(), name="create"),
    path("", include(router.urls)),
]
