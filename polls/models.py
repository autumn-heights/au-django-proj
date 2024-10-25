import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
# A model is the single, definitive source of information about your data.
# It contains the essential fields and behaviors of the data you’re storing. 

# Create a class for the conceptual object you want to store information about
# Give it attributes...
#   - The name of the attribute will be the field name in the SQL database
#   - Using one of the django.db.models data types will let us add constraints to the field in the SQL database
#   - Each of these models.XXXField types is an instance of the Field class
#   - The optional first argument for the Field class is a human-readable name
#   - The ForeignKey class can be used to create a link between two of these conceptual objects. Pass it a reference to another class.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return "Question text: " + self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "Choice: " + self.choice_text