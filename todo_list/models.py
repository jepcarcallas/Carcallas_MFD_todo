from django.db import models

class List(models.Model):
    item = models.CharField(max_Length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item
