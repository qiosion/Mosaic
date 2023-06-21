from django.db import models
from datetime import datetime
from board.models import Board
from django.shortcuts import get_object_or_404
import os

def upload_path(instance, filename):
    # 업로드 경로를 동적으로 생성
    # 이 함수는 board_upload 필드에 설정된 업로드 경로와 동일한 경로를 반환
    board_no = instance.board_no.board_no
    board = get_object_or_404(Board, board_no=board_no)
    id = board.member
    now = datetime.today().strftime("%Y%m%d%H%M%S")
    _, extension = os.path.splitext(filename)
    return f"uploads/{id}_{now}{extension}"

def download_path(instance, filename):
    # board_no = instance.board_no.board_no
    # board = get_object_or_404(Board, board_no=board_no)
    # mos = get_object_or_404(Board, board_no=board_no)
    path = os.path.split(instance.mos_up.name)
    print("path : ", path)
    return f"mosaic/{path}"

class MosaicImg(models.Model):
    mos_no = models.AutoField(primary_key=True)
    mos_up = models.FileField(null=False, upload_to=upload_path)
    mos_down = models.FileField(max_length=255, null=True, upload_to=download_path)
    board_no = models.ForeignKey(Board, on_delete=models.CASCADE, default=None)
    # def delete(self, *args, **kwargs):
    #     if self.mos_up:
    #         os.remove(os.path.join(settings.MEDIA_ROOT, self.mos_up.path))
    #     super(MosaicImg, self).delete(*args, **kwargs)

    class Meta:
        db_table = "MosaicImg"