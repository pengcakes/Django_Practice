from django.urls import path
from . import views

# URLConf Module, looks the same as the one autogenerated in the project urls.py
# instructions for editing that folder are in the comments
urlpatterns=[
    path('hello/', views.say_hello)
]
