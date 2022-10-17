import random
import string
import time

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView
from shop.models import Card, LatestProducts, Category
from .forms import CreateCardForm


def index(request):
    context = {}
    cards = LatestProducts.objects.get_products_for_main_page('Card')
    user = request.user
    context = {'user': user, 'cards':cards, 'range': range(len(cards))}
    return render(request, '../templates/shop/shop.html', context)


def create_card(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        create_form = CreateCardForm(request.POST, request.FILES or None)
        category = request.POST.get('category')
        if create_form.is_valid():
            create_form.title = create_form.cleaned_data.get('card_name')
            create_form.description = create_form.cleaned_data.get('card_description')
            create_form.image = create_form.cleaned_data.get('card_image')
            card = create_form.save()
            card.owner = request.user
            card.creator = request.user
            card.slug = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(24))
            if category:
                card.category = categories.filter(name=category).get()
            card.save()
            return redirect("index")
        else:
            context = {"err_message": create_form.errors, "categories": categories}
            return render(request, '../templates/shop/create_page.html', context)
    else:
        context = {"err_message": None, "categories": categories}
        return render(request, '../templates/shop/create_page.html', context)


class CardDetailView(DetailView):
    queryset = Card.objects.all()
    template_name = '../templates/shop/card_detail.html'
    slug_url_kwarg = 'slug'