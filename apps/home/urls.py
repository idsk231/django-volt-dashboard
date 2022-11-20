# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('transactions.html', views.transactions, name='transactions'),
    path('dashboard.html', views.pages, name='pages'),
    path('settings.html', views.pages, name='pages'),
]
