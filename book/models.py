
from django.db import models

CATEGORY = (
    ('business', 'ビジネス'),
    ('life', '生活'),
    ('hobby', '趣味'),
    ('other', 'その他'),
)

class Shelf(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(
        max_length=100,
        choices = CATEGORY,
        )

    def __str__(self):
        return self.title