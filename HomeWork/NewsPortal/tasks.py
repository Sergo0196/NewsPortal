from celery import shared_task
from  django.conf import settings
from  django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Post, Category, Subscriber
from celery.schedules import crontab

import datetime




@shared_task
def send_mail_task(pk):
    post = Post.objects.get(pk=pk)
    categories = post.category.all()
    subscribers_emails = []
    for category in categories:
        subscribers_emails += category.subscriptions.values_list('user__email', flat=True)
    subscribers_emails = set(subscribers_emails)

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
        to=subscribers_emails
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def weekly_send_email_task():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(date_time__gte=last_week)
    categories = set(posts.values_list('category__category_name', flat=True))
    subscribers = set(Category.objects.filter(category_name__in=categories).values_list('subscriptions__user__email', flat=True))
    print(subscribers)

    html_content = render_to_string('daily_post.html',
                                    {
                                        'link': settings.SITE_URL,
                                        'post': posts,
                                    }
                                    )

    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()