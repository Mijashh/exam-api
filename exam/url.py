from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .views import ExamDetailsView, ExamIndexView

router = DefaultRouter()
router.register("exam-index", ExamIndexView)
router.register("exam-detail", ExamDetailsView)

urlpatterns = [
    path("", include(router.urls)),
    re_path("^auth/", include("djoser.urls")),
    re_path("auth/", include("djoser.urls.authtoken")),
]
