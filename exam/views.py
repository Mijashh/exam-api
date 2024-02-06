from rest_framework import viewsets

from .models import ExamDetail, ExamIndex
from .serializers import ExamDetailsSerializer, ExamIndexSerializer


class ExamIndexView(viewsets.ModelViewSet):
    queryset = ExamIndex.objects.all()
    serializer_class = ExamIndexSerializer
    lookup_field = 'slug'
    
class ExamDetailsView(viewsets.ModelViewSet):
    queryset = ExamDetail.objects.all()
    serializer_class = ExamDetailsSerializer
    lookup_field = 'index__slug'
