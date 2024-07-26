from django.db import models

class Question(models.Model):
    Keyword = models.CharField(max_length=200)
    Description = models.TextField()

    def __str__(self):
        return self.Keyword

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    Response = models.TextField()
    attachment = models.FileField(upload_to='answer_attachments/', blank=True, null=True)

    def __str__(self):
        return self.Response

class Attachment(models.Model):
    question = models.ForeignKey(Question, related_name='attachments', on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments/')
