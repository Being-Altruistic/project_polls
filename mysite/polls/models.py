from django.db import models

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__ (self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text

'''
    creating a foreign key of votes into Question
    ForeignObjectKey( question class object)
    The foreign has 1-to-1 relation, where..
    1 question has 1 set of choice text.
'''





# remember to do migrations