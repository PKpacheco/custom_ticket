# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Customization, TicketTemplate, CustomEmail

admin.site.register(Customization)
admin.site.register(TicketTemplate)
admin.site.register(CustomEmail)
