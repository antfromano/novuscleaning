from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})

def services(request):
    return render(request, 'services.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # send Contact Us Send Message email
        send_mail(
            'Contact Us - Novus Clean message from ' + name, # subject
            message, # message
            email, # from email
            ['antfromano@gmail.com', 'afromano@gmail.com'], # to email
        )
        return render(request, 'contact.html', {'name': name})
    else:
        return render(request, 'contact.html', {})
