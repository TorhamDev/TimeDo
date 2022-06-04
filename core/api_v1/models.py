from django.db import models
from django.utils.translation import gettext_lazy as _
from string import ascii_uppercase, ascii_lowercase, digits
from random import choices


def create_short_link_for_timer(link_length: int) -> str:
    ascii_chars = list(ascii_uppercase + ascii_lowercase + digits)
    random_link = ""
    while True:
        random_link = choices(ascii_chars, k=link_length)
        if Timer.objects.filter(short_link=random_link).exists():
            continue
        else:
            break

    return "".join(random_link)


class Timer(models.Model):

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
    end_time = models.DateTimeField(
        blank=True,
        null=True,
        help_text=_("end time"),
    )
    is_archive = models.BooleanField(
        default=False,
        help_text=_("Is this timer archived?"),
    )
    short_link = models.CharField(
        max_length=15,
        help_text=_("timer short link (optional)"),
        blank=True,
        default="",
    )
    todo = models.ManyToManyField(
        to='ToDo',
        related_name='todo',
        blank=True,
        null=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        help_text=_("create time"),
    )
    updated = models.DateTimeField(
        auto_now=True,
        help_text=_("update time"),
    )

    def save(self, *args, **kwargs):
        if len(self.short_link) <= 1:
            self.short_link = create_short_link_for_timer(5)

        super(Timer, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class ToDo(models.Model):

    discription = models.CharField(max_length=200)
    is_done = models.BooleanField(help_text=_("Is this ToDo done?"))
    is_archive = models.BooleanField(
        default=False,
        help_text=_("Is this ToDo archived?"),
    )
