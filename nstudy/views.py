from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
# Create your views here.
def home(request):
    return render(request,'index.html')

def courses(request):
    return  render (request,'courses.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contact(request):
    return render (request,'contactus.html')

def team(request):
    return render(request,'team.html')

def privacypolicy(request):
    return render (request,'privacy.html')

def terms(request):
    return render (request, 'terms.html')

def doubts(request):
    return render(request,'doubts.html')

def practice(request):
    return render(request,'practice.html')
def testseries(request):
    return render(request,'test-series.html')

def coursesdetails(request):
    return render(request,'courses-details.html')

def gallery(request):
    return render(request,'Gallery.html')

def studymaterials(request):
    return render(request,'study-materials.html')



# start backend 
def contact1(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        insert = Contact(name=name,email=email,phone=phone,message=message)
        insert.save()
        messages.success(request, "Your Message sent successfully..")
        return redirect('/contact/')

    else:
        messages.error(request, "Something went wrong while sending your message.")
        return redirect('/contact/')
