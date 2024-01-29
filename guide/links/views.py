from django.shortcuts import render
from django.views import View

class LinksView(View):
    def get(self, request):
        return render(request, './links.html')