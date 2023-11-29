from django.shortcuts import render, redirect

import tenant
from .forms import TenantForm
from django.contrib import messages
from .models import Tenant


def tenants(request):
    all_tenants = Tenant.objects.all()
    context = {"tenants": all_tenants}
    return render(request, 'tenants/tenant_list.html', context)


def add_tenant(request):
    if request.method == "POST":
        form = TenantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tenant saved successfully')
            return redirect("tenant-create-url")
        else:
            messages.error(request, 'Tenant saving failed')
            return redirect("tenant-create-url")
    else:
        form = TenantForm()
    return render(request, 'tenants/add_tenant.html', {'form': form})


def update_tenant(request, pk):
    tenant = Tenant.objects.get(id=pk)
    if request.method == "POST":
        tenant_first_name = request.POST.get('first_name')
        tenant_last_name = request.POST.get('last_name')
        tenant_email = request.POST.get('email')
        tenant_phone_number = request.POST.get('phone_number')
        tenant_zip_code = request.POST.get('zip_code')
        tenant.first_name = tenant_first_name
        tenant.last_name = tenant_last_name
        tenant.email = tenant_email
        tenant.phone_number = tenant_phone_number
        tenant.zip_code = tenant_zip_code
        tenant.save()
        messages.success(request, 'Tenant updated successfully')
        return redirect('tenant-list-url')
    return render(request, 'tenants/update_tenant.html', {'tenant': tenant})


def delete(request, pk):
    tenant = Tenant.objects.get(id=pk)
    tenant.delete()
    messages.success(request, ' Tenant deleted successfully')
    return redirect('tenant-list-url')


def detail(request, pk):
    tenant = Tenant.objects.get(id=pk)
    return render(request, 'tenants/tenant_details.html', {'tenant': tenant})

# Create your views here.
