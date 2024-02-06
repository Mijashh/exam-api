from django.utils.text import slugify
from rest_framework import serializers
from .models import ExamDetail, ExamIndex


class ExamIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamIndex
        fields = "__all__"

    def create(self, validated_data):
        validated_data["slug"] = slugify(validated_data["name"])
        instance = ExamIndex.objects.create(**validated_data)
        return instance


class ExamDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamDetail
        fields = "__all__"
