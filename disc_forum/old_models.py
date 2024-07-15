from django.db import models

class Question(models.Model):
    Keyword = models.CharField(max_length=255)
    Description = models.TextField()

    def __str__(self):
        return self.Keyword


class Attachment(models.Model):
    question = models.ForeignKey(Question, related_name='attachments', on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments/')


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    Response = models.TextField()

    def __str__(self):
        return self.Response