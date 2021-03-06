from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, state_choices, price_choices


# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,

        'state_choices': state_choices,
        'bedroom_choice': bedroom_choices,
        'price_choice': price_choices
    }
    return render(request, 'homepage.html', context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')

    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    contextt = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
    }
    return render(request, 'about.html', contextt)
