from django.shortcuts import render, get_object_or_404
from .models import Tour

def index(request):
    return render(request, 'main/index.html')

def tours(request):
    tour = Tour.objects.all()
    context = {
        'tour': tour
    }
    return render(request, 'main/tours.html', context)

def tour_detail(request,):
    tour = Tour.objects.all()
    context = {
        'tour': tour
    }
    return render(request, 'main/tour_detail.html', context)

