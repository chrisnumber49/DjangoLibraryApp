from django.db import models

# DataFlair Models


class Books(models.Model):
    title = models.CharField(max_length=50)
    picture = models.ImageField()
    author = models.CharField(max_length=30, default='anonymous')
    email = models.EmailField(blank=True)
    describe = models.TextField(default='A great book!')

    def __str__(self):
        return self.title
