from django.shortcuts import redirect, render
from .models import Image, Location,Category
from .forms import ImageForm,CategoryForm,LoctionForm
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.

def home(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    if request.method=='POST':
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'The image details has been saved succesfully')

    else:
        form=ImageForm()

    return render(request,'pict/home.html',{'images': images, 'locations': locations,'form':form})


def image_location(request, location):
    images = Image.filter_by_location(location)
    
    return render(request, 'pict/location.html', {'location_images': images})


def search_results(request):
    if 'cat' in request.GET and request.GET["cat"]:
        category = request.GET.get("cat")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        
        return render(request, 'pict/search.html', {"message": message, "images": searched_images})

def specific(request,id):
    specific_image=Image.get_image_by_id(id)

    return render(request,'pict/specific.html',{'image':specific_image})

def delete_img(request,id):
    image_delete=Image.objects.get(id=id)
    image_delete.delete()
    return redirect(home)


def update_img(request,id):
    image=Image.get_image_by_id(id)
    form=ImageForm(request.POST or None,request.FILES or None, instance=image)
    if request.method=='POST':
        if form.is_valid():
          form.save()
          return redirect(specific,id=image.id)

    return render(request,'pict/update.html',{'form':form})

    
    


def save_location(request):
    if request.method=='POST':
        if 'loc' in request.POST and request.POST['loc']:
            name=request.POST.get('loc')
            new_loc=Location(name=name)
            new_loc.save()
            return redirect(home)


def save_categor(request):
    if request.method=='POST':
        if 'cat' in request.POST and request.POST['cat']:
            name=request.POST.get('cat')
            new_cat=Category(name=name)
            new_cat.save()
            return redirect(home)