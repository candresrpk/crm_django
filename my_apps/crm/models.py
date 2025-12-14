from django.db import models
from my_apps.users.models import Profile

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['id']
        
        
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['id']
        



class Order(models.Model):
    
    class OrderStatus(models.TextChoices):
        PENDING = 'Pending'
        PROCESSING = 'Processing'
        SHIPPED = 'Shipped'
        DELIVERED = 'Delivered'
        CANCELLED = 'Cancelled'
    
    client = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING)

    def __str__(self):
        return f"Order #{self.id} by {self.client.first_name} {self.client.last_name}"
    
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ['-order_date']


class ProductOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='product_orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for Order #{self.order.id}"
    
    
    class Meta:
        verbose_name = "Product Order"
        verbose_name_plural = "Product Orders"
        ordering = ['-order_date']