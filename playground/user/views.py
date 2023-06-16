from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import views, status, generics
from .serializer import StudentUserRegistrationSerializer
from django.contrib.auth import get_user_model


class StudentUserRegistrationGenericAPIView(generics.GenericAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = StudentUserRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "user registration"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.

data = {
    "name": "First API",
    "format": "JSON",
    "category": 'http',
    "framework": "django"
}


def dummy_api(request):
    if request.method == "POST":
        pass
    if request.method == "PUT":
        pass
    if request.method == "DELETE":
        pass
    else:
        return JsonResponse(data)


class DummyRestAPIView(views.APIView):

    def get(self, request):
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        req_data = request.data
        return Response(req_data, status=status.HTTP_200_OK)

    def put(self, request):
        req_data = request.data
        return Response(req_data, status=status.HTTP_200_OK)

    def delete(self, request):
        return Response({"message": "Id is deleted"})


class DummyRestAPIIDView(views.APIView):

    def get(self, request, id):
        return Response({"id": id})
