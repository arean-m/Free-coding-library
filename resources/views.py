from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import LearningResource
from .forms import ResourceSubmissionForm  

def resource_home(request):
    if request.method == 'POST':
        form = ResourceSubmissionForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ResourceSubmissionForm()  
    
    all_resources = LearningResource.objects.filter(approved=True).order_by('-date_added')
    return render(request, 'resources/index.html', {'form': form, 'resources': all_resources})

def generate_live_admin(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "YourSecurePassword123!")
        return HttpResponse("<h1>Success! Live superuser account 'admin' created.</h1>")
    else:
        return HttpResponse("<h1>Account already exists!</h1>")