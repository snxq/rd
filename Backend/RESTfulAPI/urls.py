"""RESTful API urls
"""
from django.urls import path
from RESTfulAPI.views import Search

urlpatterns = [
    path('search/', Search.as_view()),
]
