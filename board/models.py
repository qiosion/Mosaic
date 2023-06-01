from django.db import models
from django.contrib.auth.models import User

import member
from django.contrib.auth.models import User


def upload_path(instance, filename):
    # 업로드 경로를 동적으로 생성
    # 이 함수는 board_upload 필드에 설정된 업로드 경로와 동일한 경로를 반환
    return f"uploads/{instance.board_upload.name}"


# Create your models here.
class Board(models.Model):
    board_no = models.AutoField(primary_key=True)
    board_title = models.CharField(max_length=100, null=False)
    board_content = models.TextField(null=True)
    board_upload = models.FileField(null=False, upload_to=upload_path)
    board_download = models.CharField(max_length=255, null=True, default=upload_path)
    board_date = models.DateTimeField(null=True, auto_now_add=True)  # 현재 시간
    member = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Board"