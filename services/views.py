from django.shortcuts import render

# Create your views here.
# services/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import IceCreamService
from .forms import IceCreamServiceForm

def service_list(request):
    services = IceCreamService.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

def service_detail(request, pk):
    service = get_object_or_404(IceCreamService, pk=pk)
    return render(request, 'services/service_detail.html', {'service': service})

def service_create(request):
    if request.method == 'POST':
        form = IceCreamServiceForm(request.POST)
        if form.is_valid():
            service = form.save()
            return redirect('service_detail', pk=service.pk)
    else:
        form = IceCreamServiceForm()
    return render(request, 'services/service_form.html', {'form': form})

def service_edit(request, pk):
    service = get_object_or_404(IceCreamService, pk=pk)
    if request.method == 'POST':
        form = IceCreamServiceForm(request.POST, instance=service)
        if form.is_valid():
            service = form.save()
            return redirect('service_detail', pk=service.pk)
    else:
        form = IceCreamServiceForm(instance=service)
    return render(request, 'services/service_form.html', {'form': form})

def service_delete(request, pk):
    service = get_object_or_404(IceCreamService, pk=pk)
    service.delete()
    return redirect('service_list')
