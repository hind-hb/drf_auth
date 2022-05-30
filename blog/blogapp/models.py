from django.db import models

class Party(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # user = models.ForeignKey(get_user_model())
    def __str__(self):
        return self.title