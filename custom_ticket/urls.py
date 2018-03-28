from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from events.views import HomeView

urlpatterns = [
    url(
        r'^admin/',
        admin.site.urls
    ),
    url(
        r'^$',
        HomeView.as_view(),
        name='home'
    ),
    url(
        r'customizations/',
        include(
            'customizations.urls',
            namespace='customizations'
        )
    ),
    url(
        r'events/',
        include('events.urls')
    ),
    url(
        r'mail/',
        include('mail.urls')
    ),
    url(
        r'customizations/',
        include('customizations.urls')
    ),
    url(
        '',
        include('social_django.urls', namespace='social')
    ),
    url(
        r'^accounts/login/$',
        login, name='login'
    ),
    url(
        r'^accounts/logout/$',
        logout, {'next_page': '/events/'},
        name='logout'
    ),
    url(
        r'^password_reset/$',
        login,
        name='password_reset'
    ),
]
