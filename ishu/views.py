from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import beverage,store
from.forms import beverageform

# Create your views here.
def ishuapp(request):
    drinks = beverage.objects.all()
    return render(request,'ishu/ishuapp.html', {'drinks': drinks})

def drink_detail(request,drink_id):
    drink = get_object_or_404(beverage,pk=drink_id)
    return render(request, 'ishu/drink_detail.html', {'drink': drink})

def store_view(request):
    stores= None
    if request.method == 'POST':
        form = beverageform(request.POST)
        if form.is_valid():
            beverage= form.cleaned_data['beverage']
            stores= store.objects.filter(drink_varieties = beverage)
    else:
        form= beverageform()        
    return render(request, 'ishu/storeview.html',{'stores':stores, 'form': form})