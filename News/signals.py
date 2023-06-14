from django.contrib.auth.models import User
# from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .tasks import send_notifications
from .models import PostCategory


@receiver(m2m_changed, sender=PostCategory)
def post_created(instance, **kwargs):
    if kwargs['action'] != 'post_add':
        return

    mails_list = []
    categories = instance.category.all()
    for cat_pk in categories.values_list('pk', flat=True):
        mails_list += User.objects.filter(subscriptions__category=cat_pk).values_list('email', flat=True)

    subject = f'New post in {" and ".join(categories.values_list("category", flat=True))} is published'

    text_content = (
         f'Author: {instance.author}\n'
         f'title: {instance.title}\n\n'
         f'text: {instance.preview}'
         f'link: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )

    html_content = (
         f'Author: {instance.author}<br>'
         f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
         f'{instance.title}</a>'
         f'<p>post preview:{instance.preview()}</p>'
     )

    send_notifications.delay(
        subject=subject,
        text_content=text_content,
        html_content=html_content,
        mails_list=mails_list
    )

    # for email in set(mails_list):
    #      msg = EmailMultiAlternatives(subject, text_content, None, [email])
    #      msg.attach_alternative(html_content, "text/html")
    #      msg.send()
