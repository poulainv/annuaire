from django.contrib import admin

from .models import Project
from .models import Category
from .models import SubCategory


class CategoryAdmin(admin.ModelAdmin):
     
     def has_add_permission(self, request):
        return False

     def has_change_permission(self, request):
        return False


admin.site.register(Project)
# admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory)
