from django.shortcuts import render, redirect

import tenant
from .forms import PropertyForm
from django.contrib import messages
from .models import Property


def properties(request):
    all_properties = Property.objects.all()
    context = {"properties": all_properties}
    return render(request, 'property/property_list.html', context)


def add_property(request):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Property saved successfully')
            return redirect("property-create-url")
        else:
            messages.error(request, 'Property saving failed')
            return redirect("property-create-url")
    else:
        form = PropertyForm()
    return render(request, 'property/add_property.html', {'form': form})


def update_property(request, pk):
    property = Property.objects.get(id=pk)
    if request.method == "POST":
        property_type = request.POST.get('type')
        property_address = request.POST.get('address')
        property_landlord = request.POST.get('landlord')
        property_neighbourhood = request.POST.get('neighbourhood')
        property_zip_code = request.POST.get('zip_code')
        property_description = request.POST.get('description')
        property_price = request.POST.get('price')
        property_bedrooms = request.POST.get('bedrooms')
        property_bathrooms = request.POST.get('bathrooms')
        property_image = request.FILES.get('image')
        property.type = property_type
        property.address = property_address
        property.landlord = property_landlord
        property.neighbourhood = property_neighbourhood
        property.zip_code = property_zip_code
        property.description = property_description
        property.price = property_price
        property.bedrooms = property_bedrooms
        property.bathrooms = property_bathrooms
        property.image = property_image
        property.save()
        messages.success(request, 'Property updated successfully')
        return redirect('property-list-url')
    return render(request, 'property/update_property.html', {'property': property})


def delete(request, pk):
    property = Property.objects.get(id=pk)
    property.delete()
    messages.success(request, ' Property deleted successfully')
    return redirect('property-list-url')


def detail(request, pk):
    property = Property.objects.get(id=pk)
    return render(request, 'property/property_detail.html', {'property': property})


def pay(request, pk):
    property = Property.objects.get(id=pk)
    context = {'property': property}
    return render(request, 'property/../templates/payment.html', context)

# Create your views here.
