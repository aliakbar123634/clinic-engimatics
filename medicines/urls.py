from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.medicine_list,
        name='medicine_list'
    ),

    path(
        'add/',
        views.add_medicine,
        name='add_medicine'
    ),

    path(
        'update/<int:pk>/',
        views.update_medicine,
        name='update_medicine'
    ),

    path(
        'delete/<int:pk>/',
        views.delete_medicine,
        name='delete_medicine'
    ),

    # path(
    #     'search/',
    #     views.medicine_search_page,
    #     name='medicine_search'
    # ),

    path(
        'live-search/',
        views.medicine_search,
        name='medicine_live_search'
    ),

    path(
        '<int:pk>/',
        views.medicine_detail,
        name='medicine_detail'
    ),

]


#           python manage.py runserver