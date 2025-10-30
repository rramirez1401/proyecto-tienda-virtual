from django.db import models
from django.utils import timezone
from django.conf import settings
from web.models import Flan

# Create your models here.

class Order(models.Model):

    STATUS_RESERVED = 'reserved'
    STATUS_PAID = 'paid'
    STATUS_CANCELLED = 'cancelled'

    STATUS_CHOICES = [
        (STATUS_RESERVED, 'Reservado'),
        (STATUS_PAID, 'Pagado'),
        (STATUS_CANCELLED, 'Cancelado'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_RESERVED)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField(null=True, blank=True)
    mp_preference_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Orden #{self.pk} | Estado: {self.status}"

    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    flan = models.ForeignKey(Flan, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)


    def line_total(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.flan.name}"