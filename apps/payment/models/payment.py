from django.db import models

from apps.utils.mixins import ModelMixin


class Payment(ModelMixin):
    user = models.ForeignKey('accounts.User',
                             on_delete=models.CASCADE,
                             related_name='payments')
