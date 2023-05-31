from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class customMember(AbstractUser):
    mbr_no = models.AutoField(primary_key=True)
    mbr_id = models.CharField(max_length=100, unique=True, null=False)
    mbr_pw = models.CharField(max_length=100, null=False)
    mbr_name = models.CharField(max_length=100, null=False)
    mbr_phone = models.CharField(max_length=100, null=True)
    mbr_mail = models.CharField(max_length=100, null=True)
    mbr_regi_date = models.DateTimeField(null=True, auto_now_add=True)
    mbr_author = models.CharField(max_length=100, default='user')

    groups = models.ManyToManyField(Group, verbose_name='User groups', blank=True, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, verbose_name='User permissions', blank=True,
                                               related_name='custom_users')

    class Meta:
        db_table = "Member"
"""
class customMember(AbstractUser):
    mbr_no = models.AutoField(primary_key=True)
    mbr_id = models.CharField(max_length=100, unique=True, null=False)
    mbr_pw = models.CharField(max_length=100, null=False)
    mbr_name = models.CharField(max_length=100, null=False)
    mbr_phone = models.CharField(max_length=100, null=True)
    mbr_mail = models.CharField(max_length=100, null=True)
    mbr_regi_date = models.DateTimeField(null=True, auto_now_add=True)
    mbr_author = models.CharField(max_length=100, default='user')

    class Meta:
        db_table = "Member"
"""
"""
class Member(models.Model):
    mbr_no = models.AutoField(primary_key=True)
    mbr_id = models.CharField(max_length=100, unique=True, null=False)
    mbr_pw = models.CharField(max_length=100, null=False)
    mbr_name = models.CharField(max_length=100, null=False)
    mbr_phone = models.CharField(max_length=100, null=True)
    mbr_mail = models.CharField(max_length=100, null=True)
    mbr_regi_date = models.DateTimeField(null=True, auto_now_add=True)
    mbr_author = models.CharField(max_length=100, default='user')

    class Meta:
        db_table = "Member"
"""


