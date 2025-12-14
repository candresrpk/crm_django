from django.contrib import admin
from .models import Category, Product, Order
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)
    ordering = ('id',)
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'stock')
    list_filter = ('category',)
    search_fields = ('name',)
    ordering = ('id',)
    
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'order_date', 'total_amount', 'status')
    list_filter = ('status', 'order_date')
    search_fields = ('client__user__username', 'client__user__first_name', 'client__user__last_name')
    ordering = ('-order_date',)