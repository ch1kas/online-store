from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth import get_user_model
User = get_user_model()


def send_confirmation_email(user):
    user = User.objects.get(pk=user)
    context = {
        "text_detail": "Thank you for registration!",
        "email": user.email,
        "domain": "http://localhost:8000/",
        "activation_code": user.activation_code
    }
    msg_html = render_to_string("email.html", context)
    plain_message = strip_tags(msg_html)
    subject = "Activation Account"
    to_emails = user.email
    mail.send_mail(
        subject,
        plain_message,
        "chyngyz60390@gmail.com",
        [to_emails, ],
        html_message=msg_html
    )
