from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import naive_userFilter 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
	return render(request,'accounts/dashboard.html')

# def user_admin(request,pk_test):
# 	admin = naive_user.objects.filter(username=pk_test)
# 	# print(admin)
# 	return render(request,'accounts/user_admin.html', {'user': admin} )
@login_required(login_url='login')
def user_admin(request):
	admin = naive_user.objects.all()
	# print(admin)
	
	myfilter = naive_userFilter(request.GET, queryset=admin)
	admin = myfilter.qs

	return render(request,'accounts/user_admin.html', {'user': admin, 'myfilter':myfilter} )

def user_viewer(request,pk_test):
	user_view = naive_user.objects.filter(username=pk_test)
	return render(request,'accounts/user_viewer.html')


@login_required(login_url='login')
def create_user(request):

	form = naive_userForm()
	if request.method == 'POST':
		# print("Print POST", request.POST)
		form = naive_userForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('user_admin')
	context = {'form': form}
	return render(request, 'accounts/create_user_form.html',context)

@login_required(login_url='login') 
def update_user(request,pk_test):

	user_id = naive_user.objects.get(username=pk_test)
	# print(user_id)

	form = naive_userForm(instance=user_id)
	if request.method == 'POST':
		#print("Print POST", request.POST)
		form = naive_userForm(request.POST, instance=user_id)
		if form.is_valid():
			form.save()
			return redirect('user_admin')

	context = {'form': form}
	return render(request, 'accounts/create_user_form.html',context)	

@login_required(login_url='login')
def delete_user(request,pk_test):
	user_id = naive_user.objects.get(username=pk_test)
	if request.method == 'POST':
		user_id.delete()
		return redirect('user_admin')
	context = {'user_delete_id':user_id}
	return render(request, 'accounts/delete.html', context)

def register(request):
	if request.user.is_authenticated:
		return redirect('user_admin')
	else:
		form = createuserform()

		if request.method == 'POST':
			form = createuserform(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request,'Account was created for '+user)
				return redirect('login')

		context = {'form': form}
		return render(request, 'accounts/register.html', context)


def login_admin(request):
	if request.user.is_authenticated:
		return redirect('user_admin')
	else:
		if request.method == 'POST':
			username=request.POST.get('username')
			password=request.POST.get('password')

			admin = authenticate(request, username=username, password=password)
			if admin is not None:
				login(request, admin)
				return redirect('user_admin') 
			else:
				messages.info(request,'Username OR Password incorrect')
		context = {}
		return  render(request, 'accounts/login.html', context)

@login_required(login_url='login')
def logout_admin(request):
	logout(request)
	return redirect('login')