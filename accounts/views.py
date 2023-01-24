from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	totalorders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {'orders' :orders, 'customers' :customers, 'totalorders' :totalorders, 'delivered' :delivered, 'pending' :pending}
	return render(request, 'accounts/dashboard.html', context)

def products(request):
	products = Product.objects.all()
	return render(request, 'accounts/products.html', {'products':products})

def customer(request, pk):
	customer = Customer.objects.get(id=pk)
	orders = customer.order_set.all()

	orders_count = orders.count()

	context = {'customer' :customer, 'orders' :orders, 'orders_count' :orders_count}
	return render(request, 'accounts/customer.html', context)

def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST: ', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()

	context = {'form' :form}
	return render(request, 'accounts/order_form.html', context)