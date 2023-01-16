from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import timezone
# Create your models here.

def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("Date cannot be in the past")

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completiondate = models.DateField(validators=[validate_date])
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    
