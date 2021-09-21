from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('findrestaurant', views.findrestaurant, name="findrestaurant"),
    path('bookings', views.bookings, name="bookings"),
    path('cancellings', views.cancellings, name="cancellings"),
    path('seebookings', views.seebookings, name="seebookings"),
    path('signup', views.signup, name="signup"),
    path('adminapp', views.adminapp, name="adminapp"),
    path('restaurantadmin', views.restaurantadmin, name="restaurantadmin"),
    path('signin', views.signin, name="signin"),
    path('success', views.success, name="success"),
    path('signout', views.signout, name="signout"),
    path('findmess', views.findmess, name="findmess"),
    path('bookingsmess', views.bookingsmess, name="bookingsmess"),
    path('cancellingsmess', views.cancellingsmess, name="cancellingsmess"),
    path('seebookingsmess', views.seebookingsmess, name="seebookingsmess"),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),




]
