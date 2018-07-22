from django.views import View
from onlineapp.models import College,Student
from onlineapp.serializers.serializers import CollegeSerializer,StudentSerializer,StudentDetailSerializer
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response


# class APICollegeList(View):
# 	def get(self, request):
# 		colleges = College.objects.all()
# 		serializer = CollegeSerializer(colleges,many=True)
# 		return JsonResponse(serializer.data,safe=False)
#
# 	def post(self, request):
# 		data = JSONParser().parse(request)
# 		serializer = CollegeSerializer(data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JsonResponse(serializer.data, status=201)
# 		return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def api_college_list(request):

	if request.method == 'GET':
		colleges = College.objects.all()
		serializer = CollegeSerializer(colleges,many=True)
		return JsonResponse(serializer.data,safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = CollegeSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def api_college_detail(request, pk):
	try:
		college = College.objects.get(pk=pk)
	except College.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = CollegeSerializer(college)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = CollegeSerializer(college, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		college.delete()
		return HttpResponse(status=204)

# class APICollegeDetail(View):
# 	def get(self,request,*args,**kwargs):
# 		college = get_object_or_404(College,**kwargs)
# 		serializer = CollegeSerializer(college)
# 		return JsonResponse(serializer.data, safe=False)


# def api_student_list(request,college_id):
# 	if request.method == 'GET':
# 		students = Student.objects.filter(college__id=college_id)
# 		serializer = StudentSerializer(students, many=True)
# 		return JsonResponse(serializer.data, safe=False)

class APIStudentList(APIView):

	def get_queryset(self):
		students = Student.objects.filter(college__id=self.kwargs['college_id'])
		return students

	def get(self,request,*args,**kwargs):
		students = self.get_queryset()
		serializer = StudentSerializer(students, many=True)
		return Response(serializer.data)


class APIStudentDetail(APIView):
	def get_queryset(self):
		student = Student.objects.filter(pk=self.kwargs['pk'])
		return student

	def get(self,request,*args,**kwargs):
		student = self.get_queryset()
		serializer = StudentDetailSerializer(student,many=True)
		return Response(serializer.data)