from django.urls import path
from .views import *

urlpatterns = [
    path('reg', reg),
    path('entry', entry),
    path('confirm', confirm),
    path('exit', exit),
    path('profile', profile),
    path('reset', reset),
]