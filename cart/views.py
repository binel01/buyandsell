from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import Cart, CartItem

class CartDetail(DetailView):
    model = Cart
    template_name='Cart'


class CartList(ListView):
    model = Cart
    context_object_name = 'cart'
    template_name='cart/cart_list.html'

class CreateCart(CreateView):
    model = Cart
    template_name = 'cart/cart_create.html'

