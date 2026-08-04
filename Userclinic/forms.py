# from django import forms
# from django.contrib.auth.models import User

# from .models import Profile


# class UserRegisterForm(forms.ModelForm):

#     password = forms.CharField(
#         widget=forms.PasswordInput
#     )

#     role = forms.ChoiceField(
#         choices=Profile.ROLE_CHOICES
#     )

#     phone = forms.CharField()


#     class Meta:
#         model = User

#         fields = [
#             'username',
#             'email',
#             'password'
#         ]


from django import forms
from django.contrib.auth.models import User

from .models import Profile


class UserRegisterForm(forms.ModelForm):

    password = forms.CharField(

        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter password'
            }
        )
    )

    phone = forms.CharField(

        max_length=20,

        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter phone number'
            }
        )
    )



    class Meta:

        model = User

        fields = [

            'username',
            'email',
            'password'

        ]



    # USERNAME VALIDATION
    def clean_username(self):

        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():

            raise forms.ValidationError(

                'Username already exists.'

            )

        return username




    # EMAIL VALIDATION
    def clean_email(self):

        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():

            raise forms.ValidationError(

                'Email already exists.'

            )

        return email




    # PHONE VALIDATION
    def clean_phone(self):

        phone = self.cleaned_data.get('phone')

        if Profile.objects.filter(phone=phone).exists():

            raise forms.ValidationError(

                'Phone number already exists.'

            )

        return phone




    # PASSWORD VALIDATION
    def clean_password(self):

        password = self.cleaned_data.get('password')

        if len(password) < 6:

            raise forms.ValidationError(

                'Password must be at least 6 characters.'

            )

        return password