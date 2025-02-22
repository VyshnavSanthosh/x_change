from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(User,related_name='messages_sent', on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, related_name='messages_recieved', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender}: {self.text}"
