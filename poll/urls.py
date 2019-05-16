
from django.contrib import admin
from django.urls import path
from poll.views import *


urlpatterns = [
    path('', index, name="poll-list"),
    path('<int:id>/details/', details, name="poll-details"),
    path('<int:id>/', poll, name="single_poll"),
]
