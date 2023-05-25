from django.urls import path
from . import views

# forum의 url 연결 설정
urlpatterns = [
    # 인덱스 페이지를 forum/list로 함
    # path('forum/list', views.list),
    path('', views.list, name="index"),
    path('create', views.create),
    path('read/<int:forum_id>', views.read),
    path('delete/<int:forum_id>', views.delete),
    path('update/<int:forum_id>', views.update),
]