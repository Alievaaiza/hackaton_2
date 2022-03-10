from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import now

from applications.product.models import Product

User = get_user_model()


class Order(models.Model):
    ORDER_STATUS = (
        ('IN_PROCESSING', 'in_processing'),
        ('COMPLETED', 'completed'),
        ('DECLINED', 'declined'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    status = models.CharField(max_length=30, choices=ORDER_STATUS, default='in_processing')
    total_cost = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    delivery_address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.user.email


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_product')
    quantity = models.PositiveIntegerField(default=1)
    total_cost = models.DecimalField(max_digits=100, decimal_places=2, default=1)

    def __str__(self):
        return f'{self.id}'

    def save(self, *args, **kwargs):
        self.total_cost = self.product.price * self.quantity
        super(OrderProduct, self).save(*args, **kwargs)

