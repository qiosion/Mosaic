from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create),
    path('read/<int:board_no>', views.read, name="read"),
    path('', views.list, name="list"),
]
    # 인덱스 페이지를 board/list로 함
    # path('delete/<int:board_no>', views.delete),
    # path('update/<int:board_no>', views.update),
