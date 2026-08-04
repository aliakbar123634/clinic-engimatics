from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from Userclinic.decorators import admin_required
from .models import Medicine
from .forms import MedicineForm


# ALL MEDICINES
def medicine_list(request):

    medicines = Medicine.objects.all().order_by('name')

    context = {
        'medicines': medicines
    }

    return render(
        request,
        'medicine_list.html',
        context
    )


# ADD MEDICINE
@admin_required
def add_medicine(request):

    if request.method == 'POST':

        form = MedicineForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('medicine_list')

    else:

        form = MedicineForm()

    context = {
        'form': form
    }

    return render(
        request,
        'add_medicine.html',
        context
    )


# UPDATE MEDICINE
@admin_required
def update_medicine(request, pk):

    medicine = get_object_or_404(
        Medicine,
        id=pk
    )

    if request.method == 'POST':

        form = MedicineForm(
            request.POST,
            instance=medicine
        )

        if form.is_valid():

            form.save()

            return redirect('medicine_list')

    else:

        form = MedicineForm(instance=medicine)

    context = {
        'form': form
    }

    return render(
        request,
        'update_medicine.html',
        context
    )


# DELETE MEDICINE
@admin_required
def delete_medicine(request, pk):

    medicine = get_object_or_404(
        Medicine,
        id=pk
    )

    if request.method == 'POST':

        medicine.delete()

        return redirect('medicine_list')

    context = {
        'medicine': medicine
    }

    return render(
        request,
        'delete_medicine.html',
        context
    )


def medicine_search(request):

    query = request.GET.get('q', '').strip()

    if not query:
        return JsonResponse([], safe=False)

    medicines = Medicine.objects.filter(

        Q(name__icontains=query) |
        Q(generic_name__icontains=query) |
        Q(company__icontains=query)

    ).order_by('name')[:10]

    data = []

    for medicine in medicines:
        data.append({
            'id': medicine.id,
            'name': medicine.name,
            'generic_name': medicine.generic_name or 'No Generic',
            'company': medicine.company or 'No Company',
            'price': str(medicine.price),
        })

    return JsonResponse(data, safe=False)


# MEDICINE SEARCH PAGE
def medicine_search_page(request):

    query = request.GET.get('q', '').strip()

    medicines = Medicine.objects.filter(

        Q(name__icontains=query) |
        Q(generic_name__icontains=query) |
        Q(company__icontains=query)

    ).order_by('name')

    context = {
        'medicines': medicines,
        'query': query
    }

    return render(
        request,
        'medicine_search.html',
        context
    )


# MEDICINE DETAIL
def medicine_detail(request, pk):

    medicine = get_object_or_404(
        Medicine,
        id=pk
    )

    context = {
        'medicine': medicine
    }

    return render(
        request,
        'medicine_detail.html',
        context
    )