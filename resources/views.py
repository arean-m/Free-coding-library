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
    username = "admin"
    # We are using a fresh, clear password string here
    password = "LetMeInSecure2026!" 
    
    # This will find the admin or create it if it disappeared
    user, created = User.objects.get_or_create(username=username, defaults={'email': 'admin@example.com'})
    
    # This forces the password to be exactly what is written above
    user.set_password(password)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    
    return HttpResponse(f"""
        <h1>🔐 Live Admin Account Synced!</h1>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Password:</strong> {password}</p>
        <br>
        <p>Copy the password above exactly (no spaces) and try logging in at <a href="/admin/">/admin/</a> now!</p>
    """)