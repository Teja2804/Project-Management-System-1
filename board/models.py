from django.db import models

# Create your models here.
class Board(models.Model):
    Title = models.CharField(max_length=35)
    board_id = models.IntegerField(primary_key = True)

    def __str__(self) :
        return self.Title


class InsideBoard(models.Model) :
    board_id = models.IntegerField()
    title_id = models.IntegerField(default=None)
    SubTitle = models.CharField(max_length=35)
    CardTitle = models.CharField(max_length=35)
    CardBody = models.TextField(max_length=500)

    def __str__(self):
        return self.CardBody
