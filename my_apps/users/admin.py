from django.contrib import admin
from .models import Profile, Profile_Category
# Register your models here.



@admin.register(Profile_Category)
class ProfileCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)
    ordering = ('id',)
    
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'category', 'addres', 'phone_number', 'email', 'birth_date')
    list_filter = ('category',)
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'email')
    ordering = ('id',)