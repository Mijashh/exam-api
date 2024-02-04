from rest_framework import serializers

from .models import ExamDetails, ExamIndex


class ExamIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamIndex
        fields = '__all__'
        
class ExamDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamDetails
        fields = '__all__'