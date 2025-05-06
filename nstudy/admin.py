from django.contrib import admin

# Register your models here.
# from .models import Contact

# admin.site.register(Contact, admin.ModelAdmin)

# class ProductAdmin(Contact,admin.ModelAdmin):
#     list_display = ('id', 'name','email','phone')

from django.contrib import admin
from .models import Contact
from .models import Course
from django.utils.html import format_html
@admin.register(Contact)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone','message', 'created_at')
    list_per_page = 1000  # ya jitna aap chahein

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 80px; width: 80px; object-fit: cover;" />', obj.image.url)
        return "No Image"

    image_tag.short_description = 'Image'

    list_display = (
        'id', 'title', 'image_tag', 'start_date', 'end_date',
        'duration', 'course_fee', 'discount', 'created_at'
    )
    list_per_page = 1000