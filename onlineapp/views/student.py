# from django.views.generic import ListView
# from onlineapp.models import Student
#
# class CollegeDetailsView(ListView):
# 	model = Student
# 	context_object_name = 'colleges'
# 	template_name = 'college_list.html'
#
# 	def get_context_data(self, **kwargs):
# 		context = super(CollegeListView, self).get_context_data(**kwargs)
# 		# context[self.context_object_name] = self.model.objects.filter(acronym='vce')
# 		# import ipdb
# 		# ipdb.set_trace()
# 		return context
from django.http import Http404
from django.views.generic import CreateView,UpdateView,DeleteView

from onlineapp.models import Student,College

from onlineapp.forms import StudentForm, MockTestForm

from django.urls import reverse_lazy

from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class CreateStudentView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
	login_url = '/login/'
	permission_required = 'onlineapp.add_student'
	permission_denied_message = "User doesn't have the permission to add a student"
	raise_exception = True
	model = Student
	template_name = 'add_student.html'
	form_class = StudentForm

	def get_context_data(self, **kwargs):
		context = super(CreateStudentView, self).get_context_data(**kwargs)
		student_form = context.get('form')
		test_form = MockTestForm()
		context.update({'student_form': student_form, 'test_form': test_form, 'title': 'Add student'})
		return context

	def post(self, request, *args, **kwargs):

		student_form = StudentForm(request.POST)
		test_form = MockTestForm(request.POST)
		college = get_object_or_404(College, pk = kwargs.get('college_id'))

		if student_form.is_valid():
			student = student_form.save(commit=False)
			student.college = college
			student.save()

			if test_form.is_valid():
				test = test_form.save(commit=False)
				test.student = student
				test.total = sum(test_form.cleaned_data.values())
				test.save()
				return redirect('onlineapp:colleges_html')


class EditStudent(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
	login_url = '/login/'
	permission_required = 'onlineapp.change_student'
	permission_denied_message = "User doesn't have the permission to edit a student"
	raise_exception = True
	model = Student
	template_name = 'add_student.html'
	form_class = StudentForm

	def get_context_data(self, **kwargs):
		context = super(EditStudent,self).get_context_data(**kwargs)
		student_form = context.get('form')
		test_form = MockTestForm(instance=self.get_object().mocktest1)
		context.update({'student_form': student_form, 'test_form': test_form, 'title': 'Edit student'})
		return context

	def post(self,request,*args,**kwargs):
		student_form = StudentForm(request.POST)
		test_form = MockTestForm(request.POST)
		college = get_object_or_404(College, pk=kwargs.get('college_id'))

		if student_form.is_valid() and test_form.is_valid():
			student = student_form.save(commit=False)
			student.college = college
			student.save()
			test = test_form.save(commit=False)
			test.student = student
			test.total = sum(test_form.cleaned_data.values())
			test.save()
			return redirect('onlineapp:colleges_html')


class DeleteStudent(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
	login_url = '/login/'
	permission_required = ['onlineapp.delete_student','onlineapp.delete_mocktest1']
	permission_denied_message = "User doesn't have the permission to delete a student"
	raise_exception = True
	model = Student
	template_name = 'delete_college.html'

	def get_context_data(self, **kwargs):
		context = super(DeleteStudent, self).get_context_data(**kwargs)
		college = get_object_or_404(College, pk=self.kwargs.get('college_id'))
		self.success_url = reverse_lazy('onlineapp:college_deta',college.id)
		context['title'] = 'Delete Student'
		return context