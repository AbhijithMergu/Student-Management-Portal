from onlineapp.models import College
from onlineapp.serializers.serializers import CollegeSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
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

@api_view(['GET', 'POST'])
def api_college_list(request):

	if request.method == 'GET':
		colleges = College.objects.all()
		serializer = CollegeSerializer(colleges,many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = CollegeSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=201)
		return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT','DELETE'])
def api_college_detail(request, pk):
	try:
		college = College.objects.get(pk=pk)
	except College.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = CollegeSerializer(college)
		return Response(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = CollegeSerializer(college, data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=400)

	elif request.method == 'DELETE':
		college.delete()
		return HttpResponse(status=204)
