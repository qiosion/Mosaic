from django.db import models

from board.models import Board

def upload_path(instance, filename):
    # 업로드 경로를 동적으로 생성
    # 이 함수는 board_upload 필드에 설정된 업로드 경로와 동일한 경로를 반환
    print('instance.board_no : ', instance.board_no)
    return f"uploads/{instance.board_no}.jpg"
    # return f"uploads/{filename}"

class MosaicImg(models.Model):
    mos_no = models.AutoField(primary_key=True)
    mos_up = models.FileField(null=False, upload_to=upload_path)
    mos_down = models.CharField(max_length=255, null=True)
    board_no = models.ForeignKey(Board, on_delete=models.CASCADE, default=None)

    class Meta:
        db_table = "MosaicImg"