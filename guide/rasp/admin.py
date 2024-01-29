from django.contrib import admin
from .models import Pair

class PairAdmin(admin.ModelAdmin):
    list_display = ('sbj', 'type', 'location')
    list_filter = ('location',)
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        
        # Exclude pairs with type "Webinar" and "Лекция LMS"
        queryset = queryset.exclude(type__in=["Webinar", "Лекция LMS"])
        
        # Exclude pairs with location "Обучение LMS"
        queryset = queryset.exclude(location="Обучение LMS")
        
        return queryset

admin.site.register(Pair, PairAdmin)
