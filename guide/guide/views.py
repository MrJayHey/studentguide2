from django.shortcuts import render, HttpResponse
from django.views import View

class Main(View):
    
    def get(self, request):
        return render(request, './main.html')
    
    def post(self, request):
        return HttpResponse('This is a POST request')