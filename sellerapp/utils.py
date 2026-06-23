import re
import secrets
import string
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def myCustomMail(subject,template,to,context):
    subject = 'Subject'
    template_str = 'sellerapp/'+ template+'.html'
    html_message = render_to_string(template_str, {'data': context})
    plain_message = strip_tags(html_message)
    from_email = 'bhavyaaanjana@gmail.com'
    send_mail(subject, plain_message, from_email, [to], html_message=html_message)

def is_strong_password(password):
    """
    Returns (True, "") if password is strong, else (False, "reason").
    Rule: min 8 chars, 1 uppercase, 1 lowercase, 1 digit, 1 special char.
    """
    if not password or len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one number."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-]", password):
        return False, "Password must contain at least one special character."
    return True, ""


def generate_strong_password(length=10):
    """
    Generates a cryptographically secure random password
    (used at registration instead of the old predictable scheme).
    """
    alphabet = string.ascii_letters + string.digits + "!@#$%&*"
    while True:
        pwd = ''.join(secrets.choice(alphabet) for _ in range(length))
        if is_strong_password(pwd)[0]:
            return pwd