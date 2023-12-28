from django.db import models

class Question(models.Model):
    question = models.TextField()
    possible_answer_1 = models.CharField(max_length=255)
    possible_answer_2 = models.CharField(max_length=255)
    possible_answer_3 = models.CharField(max_length=255)
    possible_answer_4 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    additional_info = models.TextField()
