from django.urls import path
from . import views

# forum의 url 연결 설정
urlpatterns = [
    # path('forum/list', views.list),
    path('list', views.list),
    path('create', views.create),
    path('read/<int:forum_id>', views.read),
    path('delete/<int:forum_id>', views.delete),
    path('update/<int:forum_id>', views.update),
]