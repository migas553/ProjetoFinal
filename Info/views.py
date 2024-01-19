from django.shortcuts import render

# Create your views here
def about(request):
    return render(request, 'info/about.html')

def shipping(request):
    return render(request, 'info/shipping.html')

def payment(request):
    return render(request, 'info/payment.html')

def contact(request):
    return render(request, 'info/contact.html') 