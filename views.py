from django.shortcuts import render
from .models import student
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import studentForm

# Create your views here.
def pakistan(request):
    stu = student.objects.all()
    return render(request, 'Student/home.html',{
        'students': student.objects.all()
    })
def view_student(request,id):
    stu = student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('pakistan'))


def add(request):
  if request.method == 'POST':
    form = studentForm(request.POST)
    if form.is_valid():
      new_student_number = form.cleaned_data['student_id']
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_email = form.cleaned_data['email']
      new_field_of_study = form.cleaned_data['field_of_study']
      new_gpa = form.cleaned_data['gpa']

      new_student = student(
        student_id=new_student_number,
        first_name=new_first_name,
        last_name=new_last_name,
        email=new_email,
        field_of_study=new_field_of_study,
        gpa=new_gpa
      )
      new_student.save()
      return render(request, 'Student/add.html', {
        'form': studentForm(),
        'success': True
      })
  else:
    form = studentForm()
  return render(request, 'Student/add.html', {
    'form': studentForm()
  })



def edit(request, id):
  if request.method == 'POST':
    stu = student.objects.get(pk=id)
    form = studentForm(request.POST, instance=stu)
    if form.is_valid():
      form.save()
      return render(request, 'Student/edit.html', {
        'form': form,
        'success': True
      })
  else:
    stu = student.objects.get(pk=id)
    form = studentForm(instance=stu)
  return render(request, 'Student/edit.html', {
    'form': form
  })

def delete(request,id):
  if request.method == 'POST':
    stu = student.objects.get(pk=id)
    stu.delete()
  return HttpResponseRedirect(reverse('pakistan')) 
      

