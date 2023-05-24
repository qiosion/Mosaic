from django.db import models
from django.contrib.auth.models import User

class Post(models.Model): # 게시글 하나 하나
    title = models.CharField(max_length=100) # 문자. 100개까지 저장가능
    contents = models.TextField() # 문자열. 제한이 있긴 하지만 굉장히 길다
    create_date = models.DateTimeField(auto_now_add=True) # 날짜, 시간 -> 자동으로 현재 시간을 저장
    member = models.ForeignKey(User, on_delete=models.CASCADE)