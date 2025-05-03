from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('contact/',views.contact,name="contact"),
    path('team/',views.team,name="team"),
    path('privacypolicy/', views.privacypolicy,name="privacypolicy"),
    path('terms/',views.terms,name="terms"),
   
]