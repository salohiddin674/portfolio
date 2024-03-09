from django.db import models

class Banner(models.Model):
    img = models.ImageField(upload_to='banner_photo')
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)


class Resume(models.Model):
    img = models.ImageField(upload_to='resume_photo')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    title1 = models.CharField(max_length=255)



class Bio(models.Model):
    full_name = models.CharField(max_length=255)
    date_brith = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


class Info(models.Model):
    name = models.CharField(max_length=20)
    text = models.TextField(max_length=255)


class People_saya(models.Model):
    img = models.ImageField(upload_to='people_say_photo')
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()

class Info1(models.Model):
    email = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
