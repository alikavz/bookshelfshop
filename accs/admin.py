from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import Usercreation, UserChangeForm
from .models import Customizeuser


class Customadmin(UserAdmin):
    add_form = Usercreation
    form = UserChangeForm
    model = Customizeuser
    list_display = ['username', 'email', 'sen', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('sen',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('sen',)}),
    )


admin.site.register(Customizeuser, Customadmin)
