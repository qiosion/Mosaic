from django.db import models

from board.models import Board

def upload_path(instance, filename):
    # 업로드 경로를 동적으로 생성
    # 이 함수는 board_upload 필드에 설정된 업로드 경로와 동일한 경로를 반환
    board_no = str(instance.board_no.board_no).zfill(8)
    return f"uploads/{board_no}.jpg"

def download_path(instance, filename):
    board_no = str(instance.board_no.board_no).zfill(8)
    print('board_no.board_no : ', board_no)
    return f"uploads/mosaic_{board_no}.jpg"

class MosaicImg(models.Model):
    mos_no = models.AutoField(primary_key=True)
    mos_up = models.FileField(null=False, upload_to=upload_path)
    mos_down = models.FileField(max_length=255, null=True, upload_to=download_path)
    board_no = models.ForeignKey(Board, on_delete=models.CASCADE, default=None)

    class Meta:
        db_table = "MosaicImg"