from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):

    class Meta:

        model = Patient

        fields = '__all__'

        def clean_phone(self):

            phone = self.cleaned_data.get('phone')

            if Patient.objects.filter(phone=phone).exists():

                raise forms.ValidationError(
                   'This phone number already exists.'
                )

            return phone    