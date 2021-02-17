from django.shortcuts import render
from .models import Student_detail

# Create your views here.
def home(request):
    details = Student_detail.objects.all().order_by("student_id")
    

    return render(request, 'registration/home.html', {'details': details})
