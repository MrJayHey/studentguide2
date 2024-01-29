from django.shortcuts import render
from django.views import View
from .models import Pair
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render

class RaspView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        # Handle the case when the user is not authenticated
        # For example, redirect to the login page or display an error message
        return render(self.request, 'auth/login.html')

    def get(self, request):
        user = request.user
        group = user.study_group
        pairs = Pair.objects.filter(group=group)
        monday = Pair.objects.filter(day='1', group=group)
        tuesday = Pair.objects.filter(day='2', group=group)
        wednesday = Pair.objects.filter(day='3', group=group)
        thursday = Pair.objects.filter(day='4', group=group)
        friday = Pair.objects.filter(day='5', group=group)
        saturday = Pair.objects.filter(day='6', group=group)
        context = {'pairs': pairs,
                   'monday': monday,
                   'tuesday': tuesday,
                   'wednesday': wednesday,
                   'thursday': thursday,
                   'friday': friday,
                   'saturday': saturday,
                   }
        return render(request, 'schedule.html', context)