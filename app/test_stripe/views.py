from django.http import JsonResponse
import stripe
import json

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Item


class ItemListView(generic.ListView):
    model = Item
    context_object_name = 'item_list'
    template_name = 'test_stripe/item_list_view.html'


class ItemDetailView(generic.DetailView):
    model = Item
    template_name = 'test_stripe/item_detail_view.html'
    pk_url_kwarg = 'id'


class CreateCheckoutSessionView(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        item = Item.objects.get(id=self.kwargs["id"])
        domain = 'http://epetrishchev.pythonanywhere.com/'
        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
        if settings.DEBUG:
            domain = 'http://127.0.0.1:8000'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item.name,
                        },
                        'unit_amount': int(item.price * 100),
                    },
                    'quantity': 1,
                }
            ],
            mode='payment',
            success_url=request.build_absolute_uri(
                reverse('succes')) + "?session_id={CHECKOUT_SESSION_ID}"
        )
        return JsonResponse(checkout_session)


@csrf_exempt
def create_checkout_session(request, id):
    item = get_object_or_404(Item, pk=id)

    stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('succes')) + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse('failed')),
    )
    print(JsonResponse({'sessionId': checkout_session['id']}))
    return JsonResponse({'sessionId': checkout_session['id']})


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_TEST_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)


class SessionCheckoutSuccess(generic.TemplateView):
    template_name = 'test_stripe/success.html'


class SessionCheckoutFailed(generic.TemplateView):
    template_name = 'test_stripe/failed.html'
