from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import requests
from requests.auth import HTTPBasicAuth
import json
from products import utils
from orders.models import Order
from django.http import HttpResponse
# Create your views here.

klarna_un = settings.KLARNA_UN
klarna_pw = settings.KLARNA_PW


def orders(request):
    return render(request, 'orders/orders.html')


@csrf_exempt
def register_order(request):
    """ View that recives a Push request from klarna once a order has been created
    and payment is made. This function then checks if the order exists in the
    database, if it does it calls Klarna and acknowledges the order, and if not
    it creates the order and then acknowledges the order """
    print(request.headers)
    print('\n*BODY')
    print(request.body)
    print(request['sid'])
    auth = HTTPBasicAuth(klarna_un, klarna_pw)
    headers = {'content-type': 'application/json'}
    if request.POST.get('sid'):
        order_id = request.POST.get('sid')
        response = requests.get(
            settings.KLARNA_BASE_URL + '/ordermanagement/v3/orders/' +
            order_id,
            auth=auth,
            headers=headers,
        )
        klarna_order = response.json()
        klarna_order['order_id']
        if Order.objects.filter(order_id = klarna_order['order_id']).count() == 1:
            requests.POST(
                settings.KLARNA_BASE_URL + '/ordermanagement/v3/orders/' +
                order_id + '/acknowledge',
                auth=auth,
                headers=headers,
            )
        else:
            order = Order(
                order_id=klarna_order['order_id'],
                status=klarna_order['status'],
                given_name=klarna_order['billing_address']['given_name'],
                family_name=klarna_order['billing_address']['family_name'],
                email=klarna_order['billing_address']['email'],
                phone_number=klarna_order['billing_address']['phone'],
                country=klarna_order['billing_address']['country'],
                postcode=klarna_order['billing_address']['postal_code'],
                town_or_city=klarna_order['billing_address']['city'],
                street_address1=klarna_order['billing_address']['street_address'],
                order_total=klarna_order['order_amount'],
                klarna_line_items=klarna_order['order_lines']
            )
            order.save()
            requests.POST(
                    settings.KLARNA_BASE_URL + '/ordermanagement/v3/orders/' +
                    order_id + '/acknowledge',
                    auth=auth,
                    headers=headers,
                )
    return HttpResponse()

#    print('RECEIVED REQUEST =)')
#    print(request.method)
#    print('\n*HEADERS')
#    print(request.headers)
#    print('\n*BODY')
#   print(request.body)
#    if request.POST:
#        print(request.POST, request.headers)
#
#    return render(request, 'orders/orders.html')
