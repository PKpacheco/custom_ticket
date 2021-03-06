from django.conf.urls import url
from django.views.generic import TemplateView
from .views import (
    accept_webhook,
    GetEmailTest,
    get_pdf_ticket,
    email_preview_pdf

)

urlpatterns = [
    url(
        r'^mail/',
        accept_webhook,
        name='mail'),
    url(
        r'^(?P<pk>[0-9]+)/generate_pdf_ticket$',
        get_pdf_ticket,
        name='generate_pdf'
    ),
    url(
        r'^(?P<pk>[0-9]+)/email_preview_pdf$',
        email_preview_pdf,
        name='email_preview'
    ),
    url(
        r'^sent-mail-success/$',
        TemplateView.as_view(
            template_name='mail/successfully_mail.html'),
        name='successfully_mail'
    ),
    url(
        r'^(?P<pk>[0-9]+)/form_send_mail$',
        GetEmailTest.as_view(),
        name='form_send_mail'
    ),
]
