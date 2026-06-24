from django.contrib import admin
from .models import LearningResource

class LearningResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'approved', 'date_added')
    
    list_editable = ('approved',)
    
    list_filter = ('approved', 'topic')

admin.site.register(LearningResource, LearningResourceAdmin)

def generate_live_admin(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "YourSecurePassword123!")
        return HttpResponse("<h1>Success! Live superuser account 'admin' created.</h1>")
    else:
        return HttpResponse("<h1>Account already exists!</h1>")