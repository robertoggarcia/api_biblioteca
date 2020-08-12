from biblioteca.celery import app
from django.core.mail import EmailMultiAlternatives


@app.task(name='email-task')
def send_mail(email):
    msg = EmailMultiAlternatives('Correo de Bienvenida', 'Bienvenido', 'hola@biblioteca.com', [email])
    msg.attach_alternative('<p>Hola bienvenido al sistema</p>', "text/html")
    msg.content_subtype = "html"
    msg.send()
