from django.db import models

class Maqola(models.Model):
    WORLD='world'
    LOCAL='local'
    SPORT='sport'

    TAG=(
        (WORLD,'world'),
        (LOCAL,'local'),
        (SPORT,'sport')
    )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255,)
    image=models.ImageField()
    tag = models.CharField(max_length=10, choices=TAG,null=True,blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        return self.image.url
    def __str__(self):
        return f'{self.id}--{self.title}'
