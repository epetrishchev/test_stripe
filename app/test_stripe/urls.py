from django.urls import path

from . import views

urlpatterns = [
    path('', views.ItemListView.as_view(), name='home'),
    path('item/<id>', views.ItemDetailView.as_view(), name='item'),
    path('succes/', views.SessionCheckoutSuccess.as_view(), name='succes'),
    path('failed', views.SessionCheckoutFailed.as_view(), name='failed'),
    path('buy/<id>',
         views.CreateCheckoutSessionView.as_view(), name='buy'),
    path('config/', views.stripe_config, name='config'),
]
