from django.shortcuts import render, redirect
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
    
    return render(request, 'resources/index.html', {
        'resources': all_resources,
        'form': form
    })