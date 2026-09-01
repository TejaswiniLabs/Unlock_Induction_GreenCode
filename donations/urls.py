from django.urls import path
from . import views


urlpatterns = [

    path(
        'donor/',
        views.donor_dashboard,
        name='donor_dashboard'
    ),

    path(
        'donor/add/',
        views.add_donation,
        name='add_donation'
    ),

    path(
        'volunteer/',
        views.volunteer_dashboard,
        name='volunteer_dashboard'
    ),

    path(
        'available/',
        views.available_donations,
        name='available_donations'
    ),

    path(
        '<int:donation_id>/claim/',
        views.claim_donation,
        name='claim_donation'
    ),

    path(
        'claimed/',
        views.claimed_donations,
        name='claimed_donations'
    ),

    path(
        '<int:donation_id>/collected/',
        views.mark_collected,
        name='mark_collected'
    ),

    path(
        '<int:donation_id>/distributed/',
        views.mark_distributed,
        name='mark_distributed'
    ),
]