from django.shortcuts import render

from django.views import View

class TeachersView(View):
    def get(self, request):
        return render(request, './teachers.html')