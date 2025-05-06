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
    path('doubts/',views.doubts,name="doubts"),
    path('practice/',views.practice,name="practice"),
    path('test-series/',views.testseries,name="test-series"),
    path('courses-details/',views.coursesdetails,name="courses-details"),
    path('gallery/',views.gallery,name="gallery"),
    path('study-materials',views.studymaterials,name='study-materials'),
   
    path('contact1/',views.contact1,name="contact1"),
]