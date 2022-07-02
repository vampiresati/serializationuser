from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
class FirstView(APIView):

    def get(self, request, *args, **kwargs):
        return Response({'data':'helllo how are you'})
class StudentView(APIView):
    def get(self, request, pk=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(id=1)
            print(stu)
            serialzied=StudentSerializer(stu)
            print(serialzied.data)
        else:
            stu = Student.objects.all()
            print(stu)
            serialzied = StudentSerializer(stu,many=True)
            print(serialzied.data)
        json=JSONRenderer().render(serialzied.data)
        print(json)
        return Response(json)

    # def post(self, request, *args,**kwargs):
    #     print(kwargs)
    #     return Response(request.POST)
class FileUploadView(APIView):
    parser_classes = [FileUploadParser]
    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        print(file_obj)
        return Response(status=204)