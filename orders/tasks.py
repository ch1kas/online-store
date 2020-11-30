from celery import shared_task
from django.core.mail import send_mail
from .models import Order
from main.celery import app


@shared_task
def order_created(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = f"Order number {order_id}"
    message = f'Dear {order.full_name},\n\nYou have successfully placed an order.\
                Your order id is {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'chyngyz60390@gmail.com',
                          [order.email])
    print(mail_sent)
    return mail_sent
