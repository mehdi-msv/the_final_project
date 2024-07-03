from django.shortcuts import render,redirect
from website.forms import *
import sweetify
# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        post = request.POST.copy()
        post['name']= 'unknown'
        form = ContactForm(post)
        if form.is_valid():
            form.save()
            sweetify.success(request,'your ticket submitted successfully')
            return redirect('website:contact')
        else:
            sweetify.error(request,'your ticket didnt submitted')
            return redirect('website:contact')
    form = ContactForm()
    context = {'form': form}
    return render(request,'website/contact.html',context)
def newsletter_view(request):
    if request.method == 'POST' :
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request,'Your message has been sent')
            return redirect('/')
        else:
            sweetify.error(request,'Your message was not sent')
            return redirect('/')
    form = NewsletterForm()
    context = {'form': form}
    return render(request,'website/index.html',context)