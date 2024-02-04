from rest_framework import viewsets

from .models import ExamDetails, ExamIndex
from .serializers import ExamDetailsSerializer, ExamIndexSerializer


class ExamIndexView(viewsets.ModelViewSet):
    queryset = ExamIndex.objects.all()
    serializer_class = ExamIndexSerializer
    
    
class ExamDetailsView(viewsets.ModelViewSet):
    queryset = ExamDetails.objects.all()
    serializer_class = ExamDetailsSerializer
