from django import forms

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()

class TopicForm(forms.Form):
    topicname=forms.CharField(max_length=100)