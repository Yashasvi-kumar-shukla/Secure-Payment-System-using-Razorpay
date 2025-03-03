from django.shortcuts import render
from .forms import ComfyPaymentForm
import razorpay
from .models import User

# Create your views here.
def comfy_payment(request):
    if request.method == "POST":
        form = ComfyPaymentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            amount = int(float(form.cleaned_data["amount"]) * 100)  # Convert to paise
            client = razorpay.Client(auth=('API_key', 'Secret_key'))
            response_payment = client.order.create(dict(
                amount=amount,
                currency="INR",
            ))
            order_id = response_payment['id']
            #razorpay_order = client.order.fetch(order_id)
            order_status = response_payment['status']
            if order_status == 'created':
                comfy_payment = User(
                    username=name,
                    amount = amount,
                    order_id = order_id,
                )
                comfy_payment.save()
                response_payment['name'] = name
                form = ComfyPaymentForm(request.POST or None)
                return render(request, 'comfy_payment.html', {'form': form, 'payment':response_payment})

    else:
        form = ComfyPaymentForm()
    form = ComfyPaymentForm()
    return render(request, 'comfy_payment.html', {'form': form})

def payment_status(request):
    response = request.POST
    print(response)
    return render(request, 'payment_status.html') 
