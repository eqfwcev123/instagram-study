from django.urls import path

from .views import login_view

app_name = 'members'
urlpatterns = [
    path('', login_view, name='login'),
]