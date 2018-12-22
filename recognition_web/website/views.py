from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import People


def people_list(request):
    peoples = People.objects.all()
    return render(request, 'website/people/list.html', {'peoples': peoples})


def people_details(request, slug):
    people = get_object_or_404(People, slug=slug)
    return render(request, 'website/people/detail.html', {'people': people})



