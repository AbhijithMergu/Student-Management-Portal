from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def hello_world(request):
	with open('mock_results.html',"r") as f:
		text = f.readlines()

	return HttpResponse(text)


def list_colleges(request):
	# text = "<table border=1px>"
	# for x in College.objects.all():
	# 	text += "<tr><td>" + x.acronym+"</td><td>"+x.name+"</td></tr>"
	# text += "</table>"
	text=""
	for x in College.objects.all():
		text += x.acronym+"\t"+x.name+"\n"

	return HttpResponse(text, content_type="text/plain")


def sample_index(request):

	return render(request, "college_list.html", {'colleges': College.objects.values_list('acronym', 'name')})

def student_details(request):
	students = Student.objects.values_list('name','email','college__acronym','mocktest1__total')
	print(students)
	return render(request,"student_details.html",{'students': students})

def student_details2(request,id=0):
	student = Student.objects.filter(id=id).values_list('name', 'email', 'college__acronym')
	print(student)
	if len(student) == 0:
		return HttpResponse("Student details with the id: "+str(id)+" doesn't exist",content_type="text/plain")
	else:
			return render(request, "student_details.html", {'students': student})




def college_student_list(request,acronym):
	students = College.objects.filter(acronym=acronym).values_list('student__name', 'student__email',
												 'student__mocktest1__total').order_by('-student__mocktest1__total')

	return render(request,"college_summary.html",{'students':students})


def test_sessions(request):
	if 'count' in request.session:
		request.session['count'] += 1
	else:
		request.session['count'] = 1

	return HttpResponse("count : "+str(request.session['count']), content_type='text/plain')
