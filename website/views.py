from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        name == request.POST['name']
        email == request.POST['email']
        subject == request.POST['subject']
        message == request.POST['message']

        return render(request, 'contact.html', {'name': name})
    else:
        return render(request, 'contact.html', {})
