from django.contrib import admin
from .models import Cv

# Register your models here.
class CvAdmin(admin.ModelAdmin):
  list_display = ("name" , "email" , "phone", "joined_date",)

admin.site.register(Cv,CvAdmin)
