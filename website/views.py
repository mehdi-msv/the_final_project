from django.shortcuts import render
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
            
        else:
            sweetify.error(request,'your ticket didnt submitted')
    form = ContactForm()
    context = {'form': form}
    return render(request,'website/contact.html',context)