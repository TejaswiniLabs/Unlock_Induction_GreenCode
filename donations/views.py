from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Donation
from .forms import DonationForm

@login_required
def donor_dashboard(request):

    donations = Donation.objects.filter(
        donor=request.user
    ).order_by('-created_at')
    return render(
        request,
        'donor/dashboard.html',
        {
            'donations': donations
        }
    )

@login_required
def add_donation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(
                commit=False
            )
            donation.donor = request.user
            donation.save()
            return redirect(
                'donor_dashboard'
            )
    else:
        form = DonationForm()
    return render(
        request,
        'donor/add_donation.html',
        {
            'form': form
        }
    )


@login_required
def available_donations(request):
    Donation.objects.filter(
        status='available',
        available_until__lt=timezone.now()
    ).update(
        status='expired'
    )
    donations = Donation.objects.filter(
        status='available'
    ).order_by(
        'available_until'
    )
    return render(
        request,
        'volunteer/available.html',
        {
            'donations': donations
        }
    )


@login_required
def claim_donation(request, donation_id):
    donation = get_object_or_404(
        Donation,
        id=donation_id
    )
    if (
        donation.status == 'available'
        and donation.available_until > timezone.now()
    ):

        donation.volunteer = request.user
        donation.status = 'claimed'
        donation.save()
    return redirect(
        'available_donations'
    )


@login_required
def claimed_donations(request):
    donations = Donation.objects.filter(
        volunteer=request.user
    ).order_by(
        'available_until'
    )
    return render(
        request,
        'volunteer/claimed.html',
        {
            'donations': donations
        }
    )

@login_required
def mark_collected(request, donation_id):
    donation = get_object_or_404(
        Donation,
        id=donation_id,
        volunteer=request.user
    )
    donation.status = 'collected'
    donation.save()
    return redirect(
        'claimed_donations'
    )

@login_required
def mark_distributed(request, donation_id):
    donation = get_object_or_404(
        Donation,
        id=donation_id,
        volunteer=request.user
    )
    donation.status = 'distributed'
    donation.save()
    return redirect(
        'claimed_donations'
    )

@login_required
def volunteer_dashboard(request):

    donations = Donation.objects.filter(
        volunteer=request.user
    ).order_by('-created_at')

    return render(
        request,
        'volunteer/dashboard.html',
        {
            'donations': donations
        }
    )