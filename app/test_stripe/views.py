from django.http import JsonResponse
import stripe
import json

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.conf import settings
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt

from .utils.stripe_api import create_checkout_session_for_item, get_stripe_config

from .models import Item


class ItemListView(generic.ListView):
    model = Item
    context_object_name = 'item_list'
    template_name = 'test_stripe/item_list_view.html'


class ItemDetailView(generic.DetailView):
    model = Item
    template_name = 'test_stripe/item_detail_view.html'
    pk_url_kwarg = 'id'


class ItemCreaeteView(generic.CreateView):
    model = Item
    fields = '__all__'
    template_name = 'test_stripe/item_create_view.html'
    success_url = reverse_lazy('home')


class CreateCheckoutSessionView(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        item = Item.objects.get(id=self.kwargs["id"])
        checkout_session = create_checkout_session_for_item(item, request)
        return JsonResponse(checkout_session)


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = get_stripe_config()
        return JsonResponse(stripe_config, safe=False)


class SessionCheckoutSuccess(generic.TemplateView):
    template_name = 'test_stripe/success.html'


class SessionCheckoutFailed(generic.TemplateView):
    template_name = 'test_stripe/failed.html'
