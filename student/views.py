from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Student
from .forms import StudentForm
from django.views.generic.base import TemplateView
from django.core.files.base import ContentFile
# Create your views here.

def add_data(request, *args, **options):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            valfn = form.cleaned_data['first_name']
            valln = form.cleaned_data['last_name']
            valpp = form.cleaned_data['profile_picture']
            valdb = form.cleaned_data['date_of_birth']
            valsk = form.cleaned_data['skills']
            valed = form.cleaned_data['education']
            reg = StudentForm(first_name=valnm, last_name=valln, profile_picture=valpp, date_of_birth=valdb, skills=valsk, education=valed)
            reg.save()

    else:
        form = StudentForm()
    return render(request, 'student/home.html', {'form':form})

def show_data(request):
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentForm()
    else:
        form = StudentForm()
    stud = Student.objects.all()
    return render(request, 'student/Studentdata.html', {'form':form, 'stud':stud})
def update_data(request, id):
    if request.method=='POST':
        data = Student.objects.get(id=id)
        form = StudentForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        data = Student.objects.get(id=id)
        form = StudentForm(instance=data)
    return render(request, 'student/Update.html', {'form':form})

def details_view(request, id):
    stud = Student.objects.get(id=id)
    return render(request, 'student/Mydata.html', {'stud': stud})

def delete_data(request, id):
    if request.method=='POST':
        pi = Student.objects.get(id=id)
        pi.delete()
        return HttpResponseRedirect('/')