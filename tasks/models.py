from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks", null=False)
    title = models.CharField(verbose_name="Titulo", max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Data de entrega", null=False, blank=False)
    finished_at = models.DateField(null=True)

    class Meta:
        ordering = ["deadline"]

    def mark_as_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()    
            self.save()

