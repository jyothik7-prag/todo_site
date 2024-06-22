from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
# Create your models here.
from django.utils import timezone
 
 
class Todo(models.Model):
    
    title = models.CharField(max_length=100, default=None)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
 
    def __str__(self):
        return self.title
    

class Registration(models.Model):
    
    first_name = models.CharField(max_length=100, default=None)
    last_name = models.CharField(max_length=100, default=None)
    email_id = models.EmailField(max_length=100, primary_key=True)
    password = models.CharField(validators=[MinLengthValidator(8, 'the file must contain atleast 8 characters0'), RegexValidator('[+-/%]', inverse_match=True, message = 'should not contains special chanracters')])
    
    date = models.DateTimeField(default=timezone.now)
 
    def __str__(self):
        return self.email_id
