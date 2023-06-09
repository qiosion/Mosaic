from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    board_no = models.AutoField(primary_key=True)
    board_title = models.CharField(max_length=100, null=False)
    board_content = models.TextField(null=True)
    board_date = models.DateTimeField(null=True, auto_now_add=True)  # 현재 시간
    member = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    class Meta:
        db_table = "Board"