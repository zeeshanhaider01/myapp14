from django.urls import path
from app import views

urlpatterns=[
    path('foo/<usn>/<age>/',views.foo)
]