from django.contrib import admin
from .models import Boys

# Register your models here.
class BoysAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "phone", "Talent", "age", "Birth_Date")
    

admin.site.register(Boys, BoysAdmin)

