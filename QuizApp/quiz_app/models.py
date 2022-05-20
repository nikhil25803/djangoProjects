from django.db import models

# Model For Questions

class QuesModel(models.Model):
    question = models.CharField(max_length=100);
    op1 = models.CharField(max_length=100)
    op2 = models.CharField(max_length=100)
    op3 = models.CharField(max_length=100)
    op4 = models.CharField(max_length=100)
    ans = models.CharField(max_length=100)

    def __str__(self):
        return self.question