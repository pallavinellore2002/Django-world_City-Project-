

# Create your views here.
# myapp/views.py
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import City

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def city_list_view(request):
    search_query = request.GET.get('search_query', '')
    search_type = request.GET.get('search_type', '')

    if search_type == 'name':
        city_list = City.objects.filter(name__icontains=search_query)
    elif search_type == 'countrycode':
        city_list = City.objects.filter(countrycode__icontains=search_query)
    elif search_type == 'district':
        city_list = City.objects.filter(district__icontains=search_query)
    else:
        city_list = City.objects.all()

    paginator = Paginator(city_list, 10)  # Show 10 cities per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'city_list.html', {'page_obj': page_obj, 'search_query': search_query, 'search_type': search_type})