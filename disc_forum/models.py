from django.db import models

class Question(models.Model):
    Keyword = models.CharField(max_length=200)
    Description = models.TextField()

    def __str__(self):
        return self.Keyword

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    Response = models.TextField()

    def __str__(self):
        return self.Response