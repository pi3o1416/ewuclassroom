

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import jsonfield

ROLES = (('teacher' , 'Teacher'), ('student', 'Student'))

class User(AbstractUser):
    image = models.ImageField(
        blank=True
    )
    cv = models.FileField(
        blank=True
    )
    dateOfBirth = models.DateField(
        _('Date of Birth'),
        blank=True,
        default=timezone.now,
        help_text = _('Date of Birth of a user.'),
    )
    role = models.CharField(
        _('Role'),
        max_length=20,
        blank=True,
        choices=ROLES,
        help_text=_('Role of an user(Student/Teacher).'),
    )
    interest = jsonfield.JSONField(
        _('Interest'),
        blank=True,
        help_text=_('interested topic like information technology, biology, physics, number theory etc.')

    )
