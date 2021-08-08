from django.db import models

# Create your models here.
class Board(models.Model):
    Title = models.CharField(max_length=35)
    board_id = models.AutoField(primary_key = True)
    slug = models.SlugField()
   
    def __str__(self) :
        return self.Title


class InsideBoard(models.Model) :
    board_id = models.ForeignKey(Board, default=1, on_delete=models.CASCADE)
    title_id = models.IntegerField()
    SubTitle = models.CharField(max_length=35)
    CardBody = models.TextField(max_length=500)

    def __str__(self):
        return self.CardBody
