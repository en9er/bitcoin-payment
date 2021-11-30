from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from shop.models import Card, LatestProducts


def index(request):
    context = {}
    cards = LatestProducts.objects.get_products_for_main_page('Card')
    user = request.user
    context = {'user': user, 'cards':cards, 'range': range(len(cards))}
    return render(request, '../templates/shop/shop.html', context)



def add_product(request):
    return HttpResponse("Create smth")


class CardDetailView(DetailView):
    queryset = Card.objects.all()
    template_name = '../templates/shop/card_detail.html'
    slug_url_kwarg = 'slug'