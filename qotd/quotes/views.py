from django.shortcuts import render
from django.template import loader

from .models import Quote

def newest(request):
    newest_quote = Quote.objects.order_by('-published_date').first()
    context = {
        'quote': newest_quote,
    }
    return render(request, 'quotes/newest.html', context)

def index(request):
    quotes = Quote.objects.order_by('-published_date')
    context = {
        'quotes': quotes
    }
    return render(request, 'quotes/index.html', context)
