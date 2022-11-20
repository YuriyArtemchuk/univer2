from django.db import models


class Faculty(models.Model):
    # Props:
    title = models.CharField(max_length=150, null=False)
    about = models.TextField(max_length=300, null=False)
    content = models.TextField(max_length=1024, null=False)
    photo = models.FileField(upload_to="photo/", null=True)
    logo = models.FileField(upload_to="logo/", null=True)
    site = models.URLField(null=True)

    def __str__(self):
        return str(self.title)

