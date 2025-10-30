from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from django.db import transaction
from .models import Order, OrderItem
from web.models import Flan



RESERVATION_TTL_MINUTES = getattr(settings, 'RESERVATION_TTL_MINUTES', 15)

# Función para crear una reserva (orden en estado 'reserved')
def create_reservation(user, cart_items):
    expires_at = timezone.now() + timedelta(minutes=RESERVATION_TTL_MINUTES)

    # Hacemos una transacción atómica para que no haya modidificaciones en la db si es que hay fallos o no hay suficiente stock
    with transaction.atomic():
        # Creamos la orden con el tiempo de expiración, el usuario y el monto total
        order = Order.objects.create(
            user = user,
            total_amount = sum(item['subtotal'] for item in cart_items),
            status = Order.STATUS_RESERVED,
            expires_at = expires_at
        )

        # Realizamos el descuento del stock del producto y creamos los ítems de la orden
        for item in cart_items:
            flan = Flan.objects.selecto_for_update().get(pk=item['flan_id'])
            if flan.stock < item['quantity']:
                raise ValueError(f'No hay suficiente stock para el flan {flan.name}')
            
            flan.stock -= item['quantity']
            flan.save()

            #Ahora creamos el ítem de la orden
            OrderItem.objects.create(
                order = order,
                flan = flan,
                quantity = item['quantity']
                price = flan.price
            )

    return order

# Funcion para cancelar reservas expiradas
def cancel_expired_orders():
    expired_orders = Order.objects.filter(status=Order.STATUS_RESERVED, expires_at__lt=timezone.now())
    for order in expired_orders:
        for item in expired_orders.items.all():
            flan = item.flan
            flan.stock += item.quantity
            flan.save()
        order.status = Order.STATUS_CANCELLED
        order.save()