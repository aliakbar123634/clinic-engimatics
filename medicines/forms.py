from django import forms
from .models import Medicine


class MedicineForm(forms.ModelForm):

    class Meta:

        model = Medicine

        fields = '__all__'


    def clean_name(self):

        name = self.cleaned_data.get('name')

        if Medicine.objects.filter(
            name__iexact=name
        ).exists():

            raise forms.ValidationError(
                'Medicine already exists.'
            )

        return name


    def clean_price(self):

        price = self.cleaned_data.get('price')

        if price < 0:

            raise forms.ValidationError(
                'Price cannot be negative.'
            )

        return price