from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
# Create your views here.

class Search(View):
    def get(self, request):
        return JsonResponse({'code': '200'})
