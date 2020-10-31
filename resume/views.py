from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.sites.requests import RequestSite

from .models import *
from .forms import *


def resumeFill(request):
    if not request.user.is_authenticated:return redirect('userlogin')
   

    return render(request, 'resume/resume_fill.html', {

        'personform': PersonForm(),
        #'educationform': EducationForm(),
        #'projectOrJobform': ProjectOrJob(),
        
    })


def resumeView(request):
    print("entered the fn")
    if request.method == 'POST':
        print("entered postrq")
        personform = PersonForm(request.POST)
      
        if personform.is_valid():
            print("entered form")
            personform.save()

        #if educationform.is_valid():
            
           # educationform.save()
           # print("entered 1")
        #if projectOrJobform.is_valid():
           # print("entered 2")
            #projectOrJobform.save()
    site_name = RequestSite(request).domain
    person = Person.objects.all().last()
    
    print(person)
    #person1={}
    #person1["first_name"]=person.first_name
   # print(person.first_name)
    
   # education = Education.objects.all()
    #projectOrJob = ProjectOrJob.objects.all()[:5]
    

    return render(request,'resume/resume_view.html', {
    'site_name': site_name,
    'per': person,

   # 'education': education,
    #'projectOrJob': projectOrJob,

    }
    ) 

