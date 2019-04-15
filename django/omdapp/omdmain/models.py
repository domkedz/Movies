from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Movies(models.Model):
    movie_id = models.CharField(max_length=9, null=False, blank=False, verbose_name=_('movieId'))
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('title'))
    release = models.CharField(max_length=10, null=True, blank=True, verbose_name=_('release'))
    runtime = models.CharField(max_length=10, null=True, blank=True, verbose_name=_('runtime'))
    actors = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('actors'))
    boxoffice = models.CharField(max_length=10, null=True, blank=True, verbose_name=_('boxoffice'))
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,
                             verbose_name=_('user'))
