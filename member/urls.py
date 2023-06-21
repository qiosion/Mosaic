from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('delete', views.delete, name="delete"),
    path('mypage', views.update, name="mypage"),

]
# path('delete/<int:board_no>', views.delete),
# path('update/<int:board_no>', views.update),