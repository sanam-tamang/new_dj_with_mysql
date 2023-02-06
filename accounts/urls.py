
from django.urls import path
from .views import *

urlpatterns = [
    path('',UserListView.as_view()),
    path('add/',AddUserView.as_view()),
]
