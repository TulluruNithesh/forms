from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *
# Create your views here.
from app1.forms import *

def student(request):
    form=StudentForm()
    if request.method=='POST':
        form_data=StudentForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))
    return render(request,'student.html',context={'form':form})

def topic(request):
    form=TopicForm()
    if request.method=='POST':
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            topicname=form_data.cleaned_data['topicname']
            t=Topic.objects.get_or_create(topic_name=topicname)[0]
            t.save()
            return HttpResponse('Data inserted Successfully')
    return render(request,'topic.html',context={'form':form})
