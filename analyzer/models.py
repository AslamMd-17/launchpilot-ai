from django.db import models

# Create your models here.
class Analysis(models.Model):
    idea = models.TextField()
    industry = models.CharField(max_length = 100 ,blank=True)
    result = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.idea[:50]} — {self.status}"
