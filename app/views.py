from django.shortcuts import render
from django.http import HttpResponse

def foo(request,usn,age):
    # data=f"AOA! my name is {usn} and age is {age}"
    return render(request,'app/base.html',{"usn":usn,"age":age})