from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Userclinic.decorators import admin_required
from .forms import UserRegisterForm
from .models import Profile
from django.shortcuts import render
from django.contrib.auth import logout
from patients.models import Patient
from prescriptions.models import (
    Visit,
    Prescription
)

import os
import shutil

from datetime import datetime

from django.conf import settings



# @admin_required
# def register_user(request):

#     if request.method == 'POST':

#         form = UserRegisterForm(request.POST)

#         if form.is_valid():

#             user = User.objects.create_user(
#                 username=form.cleaned_data['username'],
#                 email=form.cleaned_data['email'],
#                 password=form.cleaned_data['password']
#             )

#             Profile.objects.create(
#                 user=user,
#                 role=form.cleaned_data['role'],
#                 phone=form.cleaned_data['phone']
#             )

#             return redirect('login')

#     else:

#         form = UserRegisterForm()

#     context = {
#         'form': form
#     }

#     return render(
#         request,
#         'register.html',
#         context
#     )

@admin_required
def register_user(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            user = User.objects.create_user(

                username=form.cleaned_data['username'],

                email=form.cleaned_data['email'],

                password=form.cleaned_data['password']

            )




            # ALWAYS CONSULTANT
            Profile.objects.create(

                user=user,

                role='CONSULTANT',

                phone=form.cleaned_data['phone']

            )




            messages.success(

                request,

                'Consultant account created successfully.'

            )

            return redirect('register')




        else:

            messages.error(

                request,

                'Please fix the errors below.'

            )




    else:

        form = UserRegisterForm()




    context = {

        'form': form

    }

    return render(

        request,

        'register.html',

        context

    )



def login_user(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            if user.is_superuser:
                Profile.objects.get_or_create(
                    user=user,
                    defaults={
                        'role': 'ADMIN',
                        'phone': ''
                    }
                )
            else:
                Profile.objects.get_or_create(
                    user=user,
                    defaults={
                        'role': 'CONSULTANT',
                        'phone': ''
                    }
                )

            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password') 

    return render(
        request,
        'login.html'
    )




def logout_user(request):

    if request.method == 'POST':

        logout(request)

        return redirect('login')

    return redirect('dashboard')
@login_required(login_url='login')
@never_cache
def dashboard(request):

    total_patients = Patient.objects.count()

    total_visits = Visit.objects.count()

    total_prescriptions = Prescription.objects.count()

    recent_patients = Patient.objects.all().order_by('-id')[:5]

    recent_prescriptions = Prescription.objects.select_related(
        'visit',
        'visit__patient'
    ).order_by('-id')[:5]

    context = {

        'total_patients': total_patients,

        'total_visits': total_visits,

        'total_prescriptions': total_prescriptions,

        'recent_patients': recent_patients,

        'recent_prescriptions': recent_prescriptions,

    }

    return render(
        request,
        'dashboard.html',
        context
    )


@admin_required
def backup_database(request):

    # DATABASE PATH
    db_path = settings.BASE_DIR / 'db.sqlite3'




    # BACKUP FOLDER
    backup_dir = settings.BASE_DIR / 'backups'




    # CREATE BACKUP FOLDER
    os.makedirs(

        backup_dir,

        exist_ok=True

    )




    # FILE NAME
    timestamp = datetime.now().strftime(

        '%Y_%m_%d_%H_%M_%S'

    )




    backup_file = backup_dir / f'backup_{timestamp}.sqlite3'




    # COPY DATABASE
    shutil.copy(

        db_path,

        backup_file

    )




    messages.success(

        request,

        'Database backup created successfully.'

    )




    return redirect('dashboard')




from django.shortcuts import render


def csrf_error(request, reason=""):

    return render(
        request,
        'csrf_error.html',
        status=403
    )

#    python manage.py runserver