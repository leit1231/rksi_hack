from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('login/', loginUser, name='login'),
    path('worker/', worker, name="worker")
]