from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms

# Create your views here.

#function based views
#class based views

# def home(request):
#     return HttpResponse("Hello!! This is my web page")

# def about(request):
#     return HttpResponse("this is my about page")

# def contact(request):
#     return HttpResponse("COntact us here")

def home(request):
    return render(request, "myapp/home.html")


# def form_view(request):

#     if request.method=="POST":
#         form=forms.Loginform(request.POST)
#         if form.is_valid():
#             print("Validation worked")
#             print("Name : " + form.cleaned_data['name'])
#             print("email : " + form.cleaned_data['email'])
#             print("text : " + form.cleaned_data['text'])
            

#     form=forms.Loginform
#     return render(request, 'myapp/index.html', {'form':form})


def create(request):
    if request.method=="POST":
        form=forms.Loginform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("success")
            except:
                print("error saving")
    else:
        form=forms.Loginform()
    return render(request, 'myapp/index.html', {'form':form})


def success(request):
    return render(request, 'myapp/success.html')

