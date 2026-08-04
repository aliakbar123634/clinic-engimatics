from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.patient_list,
        name='patient_list'
    ),

    path(
        'add/',
        views.add_patient,
        name='add_patient'
    ),

    path(
        '<int:pk>/',
        views.patient_detail,
        name='patient_detail'
    ),

    path(
        'update/<int:pk>/',
        views.update_patient,
        name='update_patient'
    ),

    path(
        'delete/<int:pk>/',
        views.delete_patient,
        name='delete_patient'
    ),

    path(
        'search/',
        views.patient_search,
        name='patient_search'
    ),
    path(
    'live-search/',
    views.patient_live_search,
    name='patient_live_search'
),

]