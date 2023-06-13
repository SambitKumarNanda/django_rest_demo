from rest_framework import serializers
from .models import StudentDetailModel


# create a serializer that convets a models objects into json objects

# GET
class StudentDetailModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetailModel
        # fields = ["id","name", "roll_no", "date_of_birth", "branch", "year_of_joining"]
        # fields = "__all__"
        exclude = ("id",)


class StudentDetailModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetailModel
        # fields = ["id","name", "roll_no", "date_of_birth", "branch", "year_of_joining"]
        # fields = "__all__"
        exclude = ("id", "created_at")
