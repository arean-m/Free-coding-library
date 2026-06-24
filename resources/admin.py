from django.contrib import admin
from .models import LearningResource

# Customize how the admin panel displays our database rows
class LearningResourceAdmin(admin.ModelAdmin):
    # 1. This controls which database columns show up as headers on the main table
    list_display = ('title', 'topic', 'approved', 'date_added')
    
    # 2. This magical line makes the 'approved' column a live, clickable checkbox on the main list page!
    list_editable = ('approved',)
    
    # 3. Adds a helpful filter sidebar on the right side of the screen
    list_filter = ('approved', 'topic')

# Register the model along with our new custom styling rules
admin.site.register(LearningResource, LearningResourceAdmin)