from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
from .models import Patient
from .forms import PatientForm
from Userclinic.decorators import admin_required

# LIST ALL PATIENTS
def patient_list(request):

    patients = Patient.objects.all().order_by('-id')

    context = {
        'patients': patients
    }

    return render(
        request,
        'patient_list.html',
        context
    )


# ADD PATIENT
@admin_required
def add_patient(request):

    if request.method == 'POST':

        form = PatientForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('patient_list')

    else:

        form = PatientForm()

    context = {
        'form': form
    }

    return render(
        request,
        'add_patient.html',
        context
    )


# UPDATE PATIENT
@admin_required
def update_patient(request, pk):

    patient = get_object_or_404(
        Patient,
        id=pk
    )

    if request.method == 'POST':

        form = PatientForm(
            request.POST,
            instance=patient
        )

        if form.is_valid():

            form.save()

            return redirect('patient_detail', pk=pk)

    else:

        form = PatientForm(instance=patient)

    context = {
        'form': form
    }

    return render(
        request,
        'update_patient.html',
        context
    )


# PATIENT DETAIL
def patient_detail(request, pk):

    patient = get_object_or_404(
        Patient,
        id=pk
    )

    context = {
        'patient': patient
    }

    return render(
        request,
        'patient_detail.html',
        context
    )


# DELETE PATIENT
@admin_required
def delete_patient(request, pk):

    patient = get_object_or_404(
        Patient,
        id=pk
    )

    if request.method == 'POST':

        patient.delete()

        return redirect('patient_list')

    context = {
        'patient': patient
    }

    return render(
        request,
        'delete_patient.html',
        context
    )


# SEARCH PATIENT
def patient_search(request):

    query = request.GET.get('q', '')
    print(query)
    patients = Patient.objects.filter(

        Q(name__icontains=query) |
        Q(phone__icontains=query)

    ).order_by('-id')

    context = {

        'patients': patients,
        'query': query

    }

    return render(
        request,
        'patient_search.html',
        context
    )

def patient_live_search(request):

    query = request.GET.get('q', '').strip()

    if query:
        patients = Patient.objects.filter(
            Q(name__icontains=query) |
            Q(phone__icontains=query)
        ).order_by('-id')[:10]
    else:
        patients = []

    data = []

    for patient in patients:
        data.append({
            'id': patient.id,
            'name': patient.name,
            'phone': patient.phone,
            'age': patient.age,
            'gender': patient.gender,
        })

    return JsonResponse(data, safe=False)