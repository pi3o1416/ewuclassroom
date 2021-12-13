

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name',
         'last_name', 'email', 'role', 'interest')}),
        (_('Teachers Information'), {'fields': ('image', 'cv')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {
         'fields': ('last_login', 'date_joined', 'dateOfBirth')}),
    )

    list_display = ('username', 'email', 'first_name', 'role', 'interest')
    list_filter = ('role', 'email', 'username', 'interest')
