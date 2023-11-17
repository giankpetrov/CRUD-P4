from django.urls import path
from . import views
from .views import reservation_list, update_list

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register_user"),
    path('make_reservation', views.make_reservation, name="make_reservation"),
    path('reservation_list/', views.reservation_list, name='reservation_list'),
    path('update_list/<id>', views.update_list, name='update_list'),
]
