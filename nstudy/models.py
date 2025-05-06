from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "contact"

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.CharField(max_length=50)  # Example: '6 weeks', '3 months'
    course_fee = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # in percentage
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "course"

