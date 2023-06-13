from django.urls import path
from .views import StudentDetailModelReadView, SingleStudentDetailModelReadView

urlpatterns = [
    path("student-details/", StudentDetailModelReadView.as_view(), name="student-detail-model-read-view"),
    path("student-details/<id>", SingleStudentDetailModelReadView.as_view(), name="student-detail-model-read-view"),
]
