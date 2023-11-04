from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Record
# Create your views here.
def home(request):
    #getting data from the database
    records = Record.objects.all()
    #checking if user is logging in
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You Have Been Logged In !")
            return redirect('home')
        else:
            messages.success(request,"User Not Found, Please Register First !")
            return redirect('home')
    else:
        return render(request,'home.html',{'records':records})

def login_user(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You Have Been Logged In !")
            return redirect('home')
        else:
            messages.success(request,"User Not Found, Please Register First !")
            return redirect('home')
    else:
        return render(request,'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,"You Have Been Logged Out !")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"You Have Been Successfully Registered, Please Login !")
            return redirect('login')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})

def user_record(request,pk):
    if request.user.is_authenticated:
        #get record with id
        customer_record = Record.objects.get(id=pk)
        return render(request,'record.html',{'customer_record':customer_record})
    else:
        messages.success(request,"Please Login to view this page, Thank You !")
        return redirect('home')

def delete_record(request,pk):
    if request.user.is_authenticated:
        #delete record with id
        user_delete_record = Record.objects.get(id=pk)
        user_delete_record.delete()
        messages.success(request,"Record Deleted, Thank You !")
        return redirect('home')
    else:
        messages.success(request,"Please Login to view this page, Thank You !")
        return redirect('home')

def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added, Thank You !")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "Please Login to view this page, Thank You !")
		return redirect('home')

def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated, Thank You !")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "Please Login to view this page, Thank You !")
		return redirect('home')