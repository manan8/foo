from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Setting, ContactForm, ContactMessage
from product.models import Product
from django.contrib import messages
from product.models import Category
# Create your views here.

def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    products_slider = Product.objects.all().order_by('id')
    page = 'home'
    context = {'setting' : setting,
                'page' : page,
                'category' : category,
                'products_slider' : products_slider }

    return render(request, 'home/index.html', context)
    #return HttpResponse('index page')

def aboutus(request): 
    setting = Setting.objects.get(pk=1)
    context = {'setting' : setting }
    return render(request, 'home/about.html', context)

def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Your message has been sent. Thank You!')
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.get(pk=1)
    form = ContactForm
    context = {'setting' : setting, 'form' : form }
    return render(request, 'home/contactus.html', context)
    #return HttpResponse('contact us')

def category_products(request, id, slug): 
    setting = Setting.objects.get(pk=1)
    products = Product.objects.filter(category_id=id)
    return HttpResponse(products)