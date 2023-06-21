from django.urls import path
from . import views

urlpatterns = [
    path('list', views.list, name="list"),
    path('my_list', views.my_list, name="my_list"),
    path('create', views.create, name="create"),
    path('read/<int:board_no>', views.read, name="read"),
    path('update/<int:board_no>', views.update, name="update"),
    path('delete/<int:board_no>', views.delete, name="delete"),
]
