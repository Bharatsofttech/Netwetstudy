from django.shortcuts import render,redirect

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