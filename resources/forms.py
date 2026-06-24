from django import forms
from .models import LearningResource

class ResourceSubmissionForm(forms.ModelForm):
    class Meta:
        model = LearningResource
        
        fields = ['title', 'topic', 'description', 'resource_url']
        
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full bg-gray-700 border border-gray-600 rounded-lg p-2.5 text-white focus:border-emerald-500 focus:outline-none'}),
            'topic': forms.TextInput(attrs={'class': 'w-full bg-gray-700 border border-gray-600 rounded-lg p-2.5 text-white focus:border-emerald-500 focus:outline-none', 'placeholder': 'e.g., Python, Databases'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'w-full bg-gray-700 border border-gray-600 rounded-lg p-2.5 text-white focus:border-emerald-500 focus:outline-none'}),
            'resource_url': forms.URLInput(attrs={'class': 'w-full bg-gray-700 border border-gray-600 rounded-lg p-2.5 text-white focus:border-emerald-500 focus:outline-none'}),
        }