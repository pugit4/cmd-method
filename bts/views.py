from django.shortcuts import render
from .models import Boys

# Create your views here.
def members(request):
    mymembers = Boys.objects.all()
    return render(request,"all_members.html", {"mymembers": mymembers})