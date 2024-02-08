from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import ExamDetailsView, ExamIndexView

router = DefaultRouter()
router.register("exam-index", ExamIndexView)
router.register("exam-detail", ExamDetailsView)

urlpatterns = [
    path("", include(router.urls)),
    path("token-auth/", views.obtain_auth_token),
]
