from django.shortcuts import render
from .models import Image, Location


# Create your views here.

def home(request):
    images = Image.objects.all()
    locations = Location.get_locations()

    return render(request,'pict/home.html',{'images': images[::-1], 'locations': locations})


def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'pict/location.html', {'location_images': images})


def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'pict/search_results.html', {"message": message, "images": searched_images})