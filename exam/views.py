from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import ExamDetail, ExamIndex
from .serializers import ExamDetailsSerializer, ExamIndexSerializer


class ExamIndexView(viewsets.ReadOnlyModelViewSet):
    queryset = ExamIndex.objects.all()
    serializer_class = ExamIndexSerializer
    lookup_field = "slug"
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    search_fields = {"name": ["iexact"]}
    filterset_fields = {"stream": ["iexact"], "university": ["iexact"]}
    ordering_fields = ["date"]


class ExamDetailsView(viewsets.ReadOnlyModelViewSet):
    queryset = ExamDetail.objects.all()
    serializer_class = ExamDetailsSerializer
    lookup_field = "index__slug"
