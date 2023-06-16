import django_filters
from django.shortcuts import render
from .models import StudentDetailModel
from rest_framework import status, views, generics, permissions, authentication, filters
from rest_framework.response import Response
from .serializers import StudentDetailModelListSerializer, StudentDetailModelCreateSerializer, \
    StudentDetailModelUpdateSerializer


class StudentDetailModelReadView(views.APIView):
    def get(self, request):
        queryset = StudentDetailModel.objects.all()
        data = []
        for query in queryset:
            data.append({
                "id": query.id,
                "name": query.name,
                "roll_no": query.roll_no,
                "date_of_birth": query.date_of_birth,
                "branch": query.branch,
                "year_of_joining": query.year_of_joining,
            })

        return Response({"data": data})

    def post(self, request):
        if StudentDetailModel.objects.filter(roll_no=request.data['roll_no']).exists():
            return Response({"message": "Student with this roll number already exists"},
                            status=status.HTTP_400_BAD_REQUEST)
        StudentDetailModel.objects.create(**request.data)
        return Response({"message": "okay"})


class SingleStudentDetailModelReadView(views.APIView):
    def get(self, request, id):
        try:
            query = StudentDetailModel.objects.get(id=id)
            data = {
                "id": query.id,
                "name": query.name,
                "roll_no": query.roll_no,
                "date_of_birth": query.date_of_birth,
                "branch": query.branch,
                "year_of_passing": query.year_of_joining
            }
            return Response(data)
        except Exception as e:
            return Response({"message": f"Something went wrong {e}"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        data = request.data
        query = StudentDetailModel.objects.get(id=id)
        query.name = data['name']
        query.roll_no = data['roll_no']
        query.date_of_birth = data['date_of_birth']
        query.branch = data['branch']
        query.year_of_passing = data['year_of_joining']
        query.save()
        return Response({"message": "data was updated"})

    def delete(self, request, id):
        StudentDetailModel.objects.get(id=id).delete()
        return Response({"message": "data was deleted"}, status=status.HTTP_200_OK)

    """
    
    APIVIEW
    
    """


class StudentDetailModelReadRestAPIView(views.APIView):
    def get(self, request):
        queryset = StudentDetailModel.objects.all()
        serializer = StudentDetailModelListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentDetailModelCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "data added successfully"})
        else:
            return Response(serializer.errors, status=status.HTTP_200_OK)


class StudentDetailModelUpdateRestAPIView(views.APIView):
    def get(self, request, id):
        try:
            query = StudentDetailModel.objects.get(id=id)
            serializer = StudentDetailModelListSerializer(query, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error": f"Something went wrong {e}"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            query = StudentDetailModel.objects.get(id=id)
            serializer = StudentDetailModelUpdateSerializer(data=request.data, instance=query)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "data was uploaded successfully"})
            else:
                return Response(serializer.errors, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error": f"Something went wrong, {e}"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            StudentDetailModel.objects.get(id=id).delete()
            return Response({"message": "query is deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error": f"Something went wrong, {e}"}, status=status.HTTP_400_BAD_REQUEST)


"""

GENERIC API VIEWS

"""


class StudentDetailModelReadRestGenericAPIView(generics.GenericAPIView):
    queryset = StudentDetailModel.objects.all()
    serializer_class = StudentDetailModelCreateSerializer

    def get(self, request):
        queryset = StudentDetailModel.objects.all()
        serializer = StudentDetailModelListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentDetailModelCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "data added successfully"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailModelUpdateGenericAPIView(generics.GenericAPIView):
    queryset = StudentDetailModel.objects.all()
    serializer_class = StudentDetailModelListSerializer
    permission_classes = [permissions.IsAuthenticated]
    # IsAuthenticated IsAdminUser
    authenticate_class = [authentication.BaseAuthentication, authentication.TokenAuthentication, authentication.SessionAuthentication]

    def get(self, request, id):
        try:
            query = StudentDetailModel.objects.get(id=id)
            serializer = StudentDetailModelListSerializer(query, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error": f"Something went wrong, {e}"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            query = StudentDetailModel.objects.all()
            serializer = StudentDetailModelUpdateSerializer(data=request.data, instance=query)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "data was uploaded successfully"})
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Error": f"Something went wrong,{e}"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            StudentDetailModel.objects.get(id=id).delete()
            return Response({"message": "query is deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error": f"Something went wrong, {e}"}, status=status.HTTP_400_BAD_REQUEST)


"""

LISTAPIVIEW
CREATEAPIVIEW
LISTCREATEAPIVIEW
        

"""


class StudentDetailFilter(django_filters.FilterSet):
    class Meta:
        model = StudentDetailModel
        fields = ["address"]


class StudentDetailModelListAPIView(generics.ListAPIView):
    queryset = StudentDetailModel.objects.all()
    serializer_class = StudentDetailModelListSerializer
    # Adding filter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "roll_no", "branch", "address_city", "address_state", "address_country"]
    ordering_fields = ["roll_no", "created_at"]


class StudentDetailModelCreateAPIView(generics.CreateAPIView):
    queryset = StudentDetailModel.objects.all()
    serializer_class = StudentDetailModelCreateSerializer


class StudentDetailModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = StudentDetailModel.objects.all()
    serializer_class = StudentDetailModelCreateSerializer
