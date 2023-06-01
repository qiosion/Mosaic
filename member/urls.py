from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
]
# path('delete/<int:board_no>', views.delete),
# path('update/<int:board_no>', views.update),