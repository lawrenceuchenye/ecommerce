import json
import stripe

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from apps.order.models import Order
from .cart import Cart

@csrf_exempt
def webhook(request):
    payload=request.body
    event=None
    stripe.api_key=settings.STRIPE_API_HIDDEN_KEY

    try:
      event=stripe.Event_construct_from(
       json.loads(payload),stripe.api_key
      )
    except ValueError as e:
       return HttpResponse(status=400)

    if event.type == "payment_intent.succeded":
       payement_intent=event.object.data
       print(payment_intent.id)
       order=Order.objects.get(payment_intent=payment_intent.id)
       order.paid=True
       order.save()

    return HttpResponse(status=200)
 
    
