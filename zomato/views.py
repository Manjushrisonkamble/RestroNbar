from django.forms import model_to_dict
from django.shortcuts import redirect, render
from .models import RestronBar

# Create your views here.

def zomato(request):
    if request.method=="POST":
        name= request.POST.get('name')
        rating= request.POST.get('rating')
        price= request.POST.get('price')
        add= request.POST.get('add')
        city= request.POST.get('city')
        restronbar = RestronBar(name=name, rating=rating, price=price, add=add, city=city)
        restronbar.save()
        return redirect("data")
    return render(request, "zomato.html")

def data(request):
    data = RestronBar.objects.all()
    dataContext = {"list":data} 
    return render(request, "data.html", dataContext)


def update(request, id):
    if request.method=="POST":
        name= request.POST.get('name')
        rating= request.POST.get('rating')
        price= request.POST.get('price')
        add= request.POST.get('add')
        city= request.POST.get('city')
        restronbar = RestronBar(id=id, name=name, rating=rating, price=price, add=add, city=city)
        restronbar.save()
        return redirect("data")
    
    update = RestronBar.objects.get(id=id)
    updatecontext = model_to_dict(update)
    
    return render(request, "update.html", updatecontext)
    
