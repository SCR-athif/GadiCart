from django.urls import path
from . import views
from django.contrib.auth import views as auth_view



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about' ),
    path('contact/', views.contact, name='contact' ),
    path('car_view/', views.car_view, name='car_view' ),
    path('bike_view/', views.bike_view, name='bike_view' ),
    path('other_view/', views.other_view, name='other_view' ),
    path('bike_view/<str:id>', views.bdetails, name='bdetails' ),
    path('car_view/<str:id>', views.cdetails, name='cdetails' ),
    path('other_view/<str:id>', views.odetails, name='odetails' ),
    path('car/', views.car, name='car'),
    path('bike/', views.bike, name='bike'),
    path('other/', views.other, name='other'),
    path('sell/', views.sell, name='sell' ),
    path('register/', views.register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
]