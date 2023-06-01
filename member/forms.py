from django.contrib.auth.forms import UserCreationForm
from member.models import customMember

class CustomUserCreationForm(UserCreationForm):
    def sava(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.sava()
        return user

    class Meta(UserCreationForm.Meta):
        model = customMember
        fields = UserCreationForm.Meta.fields