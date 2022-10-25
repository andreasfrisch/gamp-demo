from django.shortcuts import render
from django.template import loader

from .models import Quote

def index(request):
    latest_quote = Quote.objects.order_by('-published_date').first()
    context = {
        'latest_quote': latest_quote,
    }
    return render(request, 'quotes/index.html', context)
