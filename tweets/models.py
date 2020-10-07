from django.db import models

# Create your models here.
class Tweet(models.Model):
    # id = models.AutoField(primary_key=True) - by default
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    
    class Meta:
        db_table = 'tweets' # Migrate 

    def __str__(self):
        return f"{self.content} {self.image}"