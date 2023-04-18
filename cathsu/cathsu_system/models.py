from django.db import models


class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    picture = models.ImageField(default='newImage.jpg', upload_to='Member_pics')
    
    def __str__(self):
        return self.first_name