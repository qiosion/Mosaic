# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
#
# from member.models import customMember
#
# class CustomMemberAdmin(UserAdmin):
#     # 커스텀 관리자 설정
#     list_display = ['mbr_no', 'mbr_id', 'mbr_name', 'mbr_phone']
#     list_filter = ['mbr_author']
#
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('개인 정보', {'fields': ('email', 'mbr_name', 'mbr_phone')}),
#         ('권한', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('중요 날짜', {'fields': ('last_login', 'date_joined')}),
#     )
#
#     search_fields = ['mbr_id', 'email', 'mbr_name', 'mbr_phone']
#
# admin.site.register(customMember, CustomMemberAdmin)