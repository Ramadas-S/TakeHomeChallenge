from django.shortcuts import render
from todoapp.models import Project



def landing_page(request):
    project = Project.objects.all().order_by("-created_date")

    
    return render(request,'index.html',{'projects':project})


