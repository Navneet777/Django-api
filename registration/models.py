from django.db import models
import uuid

class Registrations(models.Model):
    token = models.UUIDField(default=uuid.uuid4, editable=False,unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
