from django.shortcuts import render,redirect
from website.forms import *
import sweetify
# Create your views here.



def contact_view(request):
    """
    View function for the contact page.
    Allows users to submit a contact form.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    # If the request method is POST, create a new ContactForm instance
    # with the POST data and validate it.
    if request.method == 'POST':
        # Create a copy of the POST data and set the 'name' field to 'unknown'
        # if it is not provided.
        post = request.POST.copy()
        if 'name' not in post:
            post['name'] = 'unknown'
        
        form = ContactForm(post)
        
        # If the form is valid, save it and display a success message.
        # Redirect to the contact page.
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Your message has been sent')
            return redirect('website:contact')
        # If the form is not valid, display an error message.
        # Redirect to the contact page.
        else:
            sweetify.error(request, 'Your message was not sent')
            return redirect('website:contact')
    
    # If the request method is not POST, create a new ContactForm instance.
    form = ContactForm()
    
    # Create a context dictionary containing the form.
    context = {'form': form}
    
    # Render the contact.html template with the context dictionary.
    return render(request, 'website/contact.html', context)




def newsletter_view(request):
    """
    View function for the newsletter sign-up page.
    Allows users to sign up for the newsletter.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    # If the request method is POST, create a new NewsletterForm instance
    # with the POST data and validate it.
    if request.method == 'POST':
        # Create a new NewsletterForm instance with the POST data
        form = NewsletterForm(request.POST)
        
        # If the form is valid, save it and display a success message.
        # Redirect to the home page.
        if form.is_valid():
            form.save()
            # Display a success message to the user
            sweetify.success(request, 'Thank you for subscribing to our newsletter')
            return redirect('/')
        # If the form is not valid, display an error message.
        # Redirect to the home page.
        else:
            sweetify.error(request, 'ERROR, Please try again')
            return redirect('/')
    
    # If the request method is not POST, create a new NewsletterForm instance.
    form = NewsletterForm()
    
    # Create a context dictionary containing the form.
    context = {'form': form}
    
    # Render the index.html template with the context dictionary.
    return render(request,'website/index.html',context)
