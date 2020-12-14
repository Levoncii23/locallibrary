from django.db import models

class MyModelName(models.Model):
    
    my_field_name = models.CharField(max_length=20, help_text="Enter field documentatiry")
