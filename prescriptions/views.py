from itertools import zip_longest

from django.http import HttpResponse
from django.template.loader import render_to_string

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from patients.models import Patient
from medicines.models import Medicine

from .models import (
    Visit,
    Prescription,
    PrescriptionItem
)

from .forms import (
    VisitForm,
    PrescriptionForm,
    PrescriptionItemForm
)


# ALL VISITS
def visit_list(request):

    visits = Visit.objects.all().order_by('-id')

    context = {
        'visits': visits
    }

    return render(
        request,
        'visit_list.html',
        context
    )


# CREATE PRESCRIPTION
def create_prescription(request):

    if request.method == 'POST':

        visit_form = VisitForm(request.POST)

        prescription_form = PrescriptionForm(request.POST)

        if visit_form.is_valid() and prescription_form.is_valid():

            # SAVE VISIT
            visit = visit_form.save(commit=False)

            visit.doctor = request.user

            visit.save()

            # SAVE PRESCRIPTION
            prescription = prescription_form.save(commit=False)

            prescription.visit = visit

            prescription.save()

            medicines = request.POST.getlist('medicine')
            dosages = request.POST.getlist('dosage')
            frequencies = request.POST.getlist('frequency')
            durations = request.POST.getlist('duration')
            notes = request.POST.getlist('notes')

            created_items = 0

            for medicine_id, dosage, frequency, duration, note in zip_longest(
                medicines,
                dosages,
                frequencies,
                durations,
                notes,
                fillvalue=''
            ):

                if not medicine_id:
                    continue

                PrescriptionItem.objects.create(

                    prescription=prescription,

                    medicine_id=medicine_id,

                    dosage=dosage,

                    frequency=frequency,

                    duration=duration,

                    notes=note

                )

                created_items += 1

            if created_items == 0:
                visit.delete()
                prescription.delete()

                context = {
                    'visit_form': visit_form,
                    'prescription_form': prescription_form,
                    'medicines': Medicine.objects.all().order_by('name'),
                    'error': 'Please add at least one medicine to the prescription.'
                }

                return render(
                    request,
                    'create_prescription.html',
                    context
                )

            return redirect(
                'prescription_detail',
                pk=prescription.id
            )

    else:

        visit_form = VisitForm()

        prescription_form = PrescriptionForm()

    context = {

        'visit_form': visit_form,
        'prescription_form': prescription_form,
        'medicines': Medicine.objects.all().order_by('name')

    }

    return render(
        request,
        'create_prescription.html',
        context
    )


# PRESCRIPTION DETAIL
def prescription_detail(request, pk):

    prescription = get_object_or_404(
        Prescription,
        id=pk
    )

    items = prescription.items.all()

    context = {

        'prescription': prescription,
        'items': items

    }

    return render(
        request,
        'prescription_detail.html',
        context
    )


# PATIENT HISTORY
def patient_history(request, patient_id):

    patient = get_object_or_404(
        Patient,
        id=patient_id
    )

    visits = patient.visits.all().order_by('-id')

    context = {

        'patient': patient,
        'visits': visits

    }

    return render(
        request,
        'patient_history.html',
        context
    )











# # PDF VIEW
# def prescription_pdf(request, pk):

#     prescription = get_object_or_404(
#         Prescription,
#         id=pk
#     )

#     items = prescription.items.all()

#     context = {

#         'prescription': prescription,
#         'items': items

#     }

#     # HTML TEMPLATE
#     html_string = render_to_string(
#         'prescription_pdf.html',
#         context
#     )

#     # RESPONSE
#     response = HttpResponse(
#         content_type='application/pdf'
#     )

#     response[
#         'Content-Disposition'
#     ] = f'attachment; filename="prescription_{prescription.id}.pdf"'

#     # GENERATE PDF
#     try:
#         from weasyprint import HTML
#     except Exception as exc:
#         raise RuntimeError(
#             'WeasyPrint is required to generate prescription PDFs. '
#             'Install it with pip and the platform-specific dependencies.'
#         ) from exc

#     HTML(
#         string=html_string,
#         base_url=request.build_absolute_uri('/')
#     ).write_pdf(response)

#     return response



# PDF VIEW
def prescription_pdf(request, pk):

    prescription = get_object_or_404(
        Prescription,
        id=pk
    )

    items = prescription.items.all()

    context = {

        'prescription': prescription,
        'items': items

    }

    return render(
        request,
        'prescription_pdf.html',
        context
    )