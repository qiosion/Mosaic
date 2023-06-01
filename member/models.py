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

    # def create_user(self, username, password=None, **extra_fields):
    #     extra_fields.setdefault('is_staff', False)
    #     extra_fields.setdefault('is_superuser', False)
    #     extra_fields.setdefault('mbr_id', username)
    #     return self._create_user(username=username, password=password, **extra_fields)

    class Meta:
        db_table = "Member"


from django.contrib.auth import get_user_model

# User = get_user_model()

# user = User.objects.create_user(mbr_id='test', mbr_pw='test', mbr_name='test')
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


