from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator
from listings.choices import bedroom_choices, state_choices, price_choices



# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    contex = {
        'listings': paged_listings

    }

    return render(request, 'listings/listings.html', contex)


def listing(request, listing_id):
    list_ing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': list_ing

    }

    return render(request, 'listings/listing.html', context)


def search(request):
    listings = Listing.objects.all()
    cont = {
        'listingss': listings,
        'state_choice': state_choices,
        'bedroom_choice': bedroom_choices,
        'price_choice': price_choices

    }
    return render(request, 'listings/search.html', cont)
