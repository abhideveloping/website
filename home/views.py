from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = Contact(name=name, email=email, date=datetime.today())
        contact.save()
    return render(request, 'home.html')

def books(request):
    return render(request, 'books.html')

def facilities(request):
    return render(request, 'facilities.html')

def about(request):
    return render(request, 'about.html')

def read1(request):
    return render(request, 'read1.html')