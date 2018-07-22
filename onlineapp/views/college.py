from django.views import View
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import Http404,HttpResponseNotFound
from onlineapp.models import College, Student
from django.shortcuts import render,get_object_or_404

from onlineapp.forms import AddCollege, StudentForm, MockTestForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# class CollegeView(View):
#
# 	def get(self, request, *args, **kwargs):
# 		colleges = College.objects.all()
#
# 		return render(
# 			request,
# 			template_name='college_list.html',
# 			context={
# 				'colleges':colleges
# 			}
# 		)


class CollegeListView(LoginRequiredMixin,ListView):
	login_url = '/login/'
	model = College
	context_object_name = 'colleges'
	template_name = 'college_list.html'

	def get_context_data(self, **kwargs):
		context = super(CollegeListView, self).get_context_data(**kwargs)
		# context[self.context_object_name] = self.model.objects.filter(acronym='vce')
		context['title'] = 'Participating Colleges'
		context['user_permissions'] = self.request.user.get_all_permissions
		return context


class CollegeDetailsView(LoginRequiredMixin, DetailView):
	login_url = '/login/'

	model = College
	context_object_name = 'students'
	template_name = 'college_details.html'

	def get_object(self, queryset=None):
		return get_object_or_404(College, **self.kwargs)

	def get_context_data(self, **kwargs):
		context = super(CollegeDetailsView, self).get_context_data(**kwargs)
		college = context.get('students')
		students = list(college.student_set.order_by('-mocktest1__total'))
		# context[self.context_object_name] = self.model.objects.filter(acronym='vce')
		context[self.context_object_name] = students
		context['title'] = 'Students of '+college.name
		context['user_permissions'] = self.request.user.get_all_permissions
		return context


class CreateCollegeView(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
	login_url = '/login/'
	permission_required = 'onlineapp.add_college'
	permission_denied_message = "User doesn't have the permission to create a college"
	raise_exception = True
	model = College
	template_name = 'add_college.html'
	form_class = AddCollege
	success_url = reverse_lazy('onlineapp:colleges_html')

	def get_context_data(self, **kwargs):
		context = super(CreateCollegeView, self).get_context_data(**kwargs)
		context['title'] = 'Add College'
		return context


class EditCollege(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
	login_url = '/login/'
	permission_required = 'onlineapp.change_college'
	permission_denied_message = "User doesn't have the permission to edit a college"
	raise_exception = True
	model = College
	template_name = 'add_college.html'
	form_class = AddCollege
	success_url = reverse_lazy('onlineapp:colleges_html')

	def get_context_data(self, **kwargs):
		context = super(EditCollege, self).get_context_data(**kwargs)
		context['title'] = 'Edit College'
		return context
	#
	# def get_object(self, queryset=None):
	# 	obj = get_object_or_404(College,**self.kwargs)
	# 	return obj


class DeleteCollege(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
	login_url = '/login/'
	permission_required = 'onlineapp.delete_college'
	permission_denied_message = "User doesn't have the permission to delete a college"
	raise_exception = True
	model = College
	template_name = 'delete_college.html'
	success_url = reverse_lazy('onlineapp:colleges_html')

	def get_context_data(self, **kwargs):
		context = super(DeleteCollege, self).get_context_data(**kwargs)
		context['title'] = 'Delete College'
		return context

	# def get_object(self, queryset=None):
	# 	obj = get_object_or_404(College, **self.kwargs)
	# 	return obj
