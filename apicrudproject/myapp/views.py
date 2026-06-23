from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from .models import student

class StudentList(APIView):
    def get(self, request):
        s = student.objects.all()
        s1 = StudentSerializer(s, many=True)
        return Response(s1.data)

    def post(self, request):
        s1 = StudentSerializer(data=request.data)
        if s1.is_valid():
            s1.save()
            return Response(s1.data, status=status.HTTP_201_CREATED)
        return Response(s1.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetails(APIView):
    def get(self, request, id):
        try:
            s = student.objects.get(id=id)
        except student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        s1 = StudentSerializer(s)
        return Response(s1.data)

    def put(self, request, id):
        try:
            s = student.objects.get(id=id)
        except student.DoesNotExist:  # Fixed: Use model class name 'student', not object instance 's'
            return Response(status=status.HTTP_404_NOT_FOUND)
        s1 = StudentSerializer(s, data=request.data)
        if s1.is_valid():
            s1.save()
            return Response(s1.data)
        return Response(s1.errors, status=status.HTTP_400_BAD_REQUEST)
