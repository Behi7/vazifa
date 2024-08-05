from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=244)
    subject = models.CharField(max_length=233)
    text = models.TextField()
    is_show = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
    

class Banner(models.Model):
    title = models.CharField(max_length=245)
    sub_title = models.CharField(max_length=255)
    body = models.TextField()


class Cell(models.Model):
    icon = models.TextField()
    title = models.CharField(max_length=244)
    info = models.TextField()


class Info(models.Model):
    phone = models.TextField(max_length=255)
    email = models.URLField(max_length=255)
    region = models.TextField()
    region_map = models.URLField(max_length=255)
    

class Link(models.Model):
    facebook = models.URLField(max_length=255)
    twitter= models.URLField(max_length=255)
    instagram = models.URLField(max_length=255)
    


