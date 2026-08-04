from django import forms

from .models import (
    Visit,
    Prescription,
    PrescriptionItem
)


class VisitForm(forms.ModelForm):

    class Meta:

        model = Visit

        fields = [
            'patient',
            'complaints',
            'diagnosis',
            'notes'
        ]


class PrescriptionForm(forms.ModelForm):

    class Meta:

        model = Prescription

        fields = [
            'instructions'
        ]


class PrescriptionItemForm(forms.ModelForm):

    class Meta:

        model = PrescriptionItem

        fields = [
            'medicine',
            'dosage',
            'frequency',
            'duration',
            'notes'
        ]