from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Customizeuser


class Usercreation(UserCreationForm):
    class Meta:
        model = Customizeuser
        fields = ('username', 'sen', 'email',)  # UserCreationForm.Meta.fields + ('sen',)


class Userchange(UserChangeForm):
    class Meta:
        model = Customizeuser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'sen', 'email',)
