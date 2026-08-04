from django.urls import path

from . import views


urlpatterns = [

    # ALL VISITS
    path(
        'visits/',
        views.visit_list,
        name='visit_list'
    ),

    # CREATE PRESCRIPTION
    path(
        'create-prescription/',
        views.create_prescription,
        name='create_prescription'
    ),

    # PRESCRIPTION DETAIL
    path(
        'prescription/<int:pk>/',
        views.prescription_detail,
        name='prescription_detail'
    ),

    # PATIENT HISTORY
    path(
        'patient-history/<int:patient_id>/',
        views.patient_history,
        name='patient_history'
    ),

    # PRESCRIPTION PDF
    path(
        'prescription/pdf/<int:pk>/',
        views.prescription_pdf,
        name='prescription_pdf'
    ),

]