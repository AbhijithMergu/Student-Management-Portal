from onlineapp.forms import SignUpForm,LoginForm
from django.views import View
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


class CreateUser(View):

	def get(self,request,*args,**kwargs):
		if request.user.is_authenticated:
			return redirect("onlineapp:colleges_html")
		form = SignUpForm()
		return render(request, template_name="registration.html", context={'form':form,'title':'User Registration'})

	def post(self, request, *args, **kwargs):
		user_form = SignUpForm(request.POST)
		if user_form.is_valid():
			user = User.objects.create_user(**user_form.cleaned_data)
			user.save()

			user = authenticate(
				request,
				username = user_form. cleaned_data['username'],
				password = user_form.cleaned_data['password']
			)

			if user is not None:
				login(request, user)
				return redirect('onlineapp:colleges_html')
			else:
				return redirect('onlineapp:signup')


class LoginUser(View):
	def get(self,request,*args,**kwargs):
		if request.user.is_authenticated:
			return redirect("onlineapp:colleges_html")

		form = LoginForm()
		return render(request,template_name="login.html",context={'form':form,'title':'User Login'})

	def post(self,request,*args,**kwargs):
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			user = authenticate(request,**login_form.cleaned_data)
			if user is not None:
				login(request,user)
				return redirect('onlineapp:colleges_html')
			else:
				return redirect('onlineapp:login')


def logout_user(request):
	logout(request)
	return redirect('onlineapp:login')
