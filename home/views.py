from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(name,email,password)
        user.save()
    return render(request,'register.html')
