from django.urls import path
from . import views

urlpatterns = [
    path('list', views.list, name="list"),
    path('create', views.create),
]
    # path('read/<int:board_no>', views.read, name="read"),
    # path('delete/<int:board_no>', views.delete),
    # path('update/<int:board_no>', views.update),
