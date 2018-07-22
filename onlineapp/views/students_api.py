from onlineapp.models import Student
from onlineapp.serializers.serializers import StudentSerializer,StudentDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class APIStudentList(APIView):

	def get_queryset(self):
		students = Student.objects.filter(college__id=self.kwargs['college_id'])
		return students

	def get(self,request,*args,**kwargs):
		students = self.get_queryset()
		serializer = StudentSerializer(students, many=True)
		return Response(serializer.data)

	def post(self, request, **kwargs):
		serializer = StudentDetailSerializer(data={**request.data, **kwargs})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIStudentDetail(APIView):

	def get(self,request,*args,**kwargs):
		student = get_object_or_404(Student,**kwargs)
		serializer = StudentDetailSerializer(student,many=False)
		if not serializer:
			return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
		return Response(serializer.data)

	def put(self, request, **kwargs):
		student_details = get_object_or_404(Student, **kwargs)
		serializer = StudentDetailSerializer(student_details, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, **kwargs):
		student_details = get_object_or_404(Student, **kwargs)
		student_details.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
