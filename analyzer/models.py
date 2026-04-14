from django.db import models
import ast
import json
class Analysis(models.Model):
    idea = models.TextField()
    industry = models.CharField(max_length=100, blank=True)
    result = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def get_result(self):
        if self.result:
            try:
                return json.loads(self.result)
            except:
                return None
        return None

    def __str__(self):
        return f"{self.idea[:50]} — {self.status}"