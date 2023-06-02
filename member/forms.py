# from django.contrib.auth.forms import UserCreationForm
# from member.models import customMember
#
# class CustomUserCreationForm(UserCreationForm):
#     def sava(self, commit=True):
#         user = super().save(commit=False)
#         if commit:
#             user.sava()
#         return user
#
#     class Meta(UserCreationForm.Meta):
#         model = customMember
#         fields = UserCreationForm.Meta.fields


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class SignupForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=False)
#
#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2', 'first_name')