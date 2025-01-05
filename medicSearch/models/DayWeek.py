from medicSearch. models import *

class DayWeek(models.model):
    name = models.CharField(null=False, max_length=20)
    status = models.TextField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
    