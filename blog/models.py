from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()

    # show correct title for admin
    def __str__(self):
        return self.title

    # display body text only 100 chars
    def summary(self):
        return self.body[:100]

    # format date
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    