from celery import shared_task
from  django.conf import settings
from  django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Post, Category, Subscriber
import datetime

@shared_task
def send_mail_task(pk):
    post = Post.objects.get(pk=pk)
    categories = post.category.all()
    subscriber = Subscriber.objects.get(pk=pk)
    title = post.title
    subscribers: list[str] = []
    for sub in subscriber:
        subscribers_users = sub.name.all()
        for sub_user in subscribers_users:
            subscribers.append(sub_user.email)
    html_content = render_to_string('post_created_email.html',
                                    {
                                        'text': f'{post.title}',
                                        'link': f'{settings.SITE_URL}/news/{pk}'
                                    }
                                    )

    msg = EmailMultiAlternatives(
        subject='title',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscriber
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

