from rest_framework import serializers
from .models import StudentDetailModel


class StudentDetailModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetailModel
        exclude = ("id")


class StudentDetailModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetailModel
        exclude = ("id", "created_at")

    def validate(self, data):
        if StudentDetailModel.objects.filter(roll_no=data['roll_no']).exists():
            return serializers.ValidationError({'message': 'student with this roll no already exists'})
        return data


class StudentDetailModelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetailModel
        exclude = ("id", "created_at")
