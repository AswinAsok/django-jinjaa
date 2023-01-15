from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path('home', views.home, name='home'),
    path('create', views.create, name='create'),
    path('update_value', views.update_value, name='update_value'),
    path('signup', views.signup, name='signup'),
    path('', views.login, name='login'),
    path('logout', views.userlogout, name='logout'),
]
