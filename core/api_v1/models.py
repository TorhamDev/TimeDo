from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Timer(models.Model):

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        max_length=80,
        help_text=_("title"),
    )
    description = models.TextField(
        help_text=_("description"),
    )
    start_time = models.DateTimeField(
        auto_now_add=True,
        help_text=_("start time"),
    )
    last_stop = models.DateTimeField(
        blank=True,
        null=True,
        help_text=_("last stop time"),
    )
    end_time = models.DateTimeField(
        blank=True,
        null=True,
        help_text=_("end time"),
    )
    is_archive = models.BooleanField(
        default=False,
        help_text=_("Is this timer archived?"),
    )
    is_stop = models.BooleanField(
        default=False,
        help_text=_("Is this timer stoped now?"),
    )
    is_end = models.BooleanField(
        default=False,
        help_text=_("Is this timer ended?"),
    )
    short_link = models.URLField(
        help_text=_("timer short link (optional)"),
        blank=True,
        default="",
    )
    todo = models.ManyToManyField(
        to='ToDo',
        related_name='todo',
        blank=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        help_text=_("create time"),
    )
    updated = models.DateTimeField(
        auto_now=True,
        help_text=_("update time"),
    )

    def __str__(self) -> str:
        return self.title


class ToDo(models.Model):

    discription = models.CharField(max_length=200)
    is_done = models.BooleanField(help_text=_("Is this ToDo done?"))
    is_archive = models.BooleanField(
        default=False,
        help_text=_("Is this ToDo archived?"),
    )

    def __str__(self) -> str:
        if len(self.discription) <= 10:
            return self.discription
        else:
            return self.discription[0:10]
