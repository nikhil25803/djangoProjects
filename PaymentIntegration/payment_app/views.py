
import re
from django.shortcuts import render
from .models import ColdCoffee
# from payment_app.models import ColdCoffee
from  . forms import CoffeePAymentForm
import razorpay
# Create your views here.

def index(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        amount = int(request.POST.get('amount')) * 100

        # Razorpay Client
        client = razorpay.Client(auth=('rzp_test_QsRJL1e3kVPX91', '0flH3cKoxVJLL1IfwqGTDJyi'))

        # Create Order
        response_payment = client.order.create(dict(amount = amount, currency = "INR"))

        # print(response_payment)

        order_id = response_payment['id']
        order_status = response_payment['status']

        if order_status=="created":
            cold_coffee = ColdCoffee(
                name = name,
                amount = amount,
                order_id = order_id,
            )
            cold_coffee.save()
            response_payment['name'] = name
            

            form = CoffeePAymentForm(request.POST or None)
            return render(request, 'coffee_payment.html', {'form':form, 'payment':response_payment,})

    form = CoffeePAymentForm()

    return render(request, 'coffee_payment.html', {'form':form})


def payment_status(request):

    response = request.POST
    print(response)

    return render(request, 'payment_status.html')