from django.db import models
from django.utils.safestring import mark_safe

# 1 - Home Page 
class Home(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=350)
    image = models.ImageField(upload_to='Home/')

    class Meta:
        verbose_name_plural = '1 - Home'

    def __str__(self):
        return self.title


# 2 - About Page 
class About(models.Model):
    description1 = models.TextField(max_length=250, verbose_name="description")
    description2 = models.TextField(max_length=350, verbose_name="description")
    description3 = models.TextField(max_length=250, verbose_name="description")
    image = models.ImageField(upload_to='About/')

    class Meta:
        verbose_name_plural = '2 - About'


# 3 - Gallery Page 
class Gallery(models.Model):
    image = models.ImageField(upload_to='Portfolio/')


    def show_photo(self):
        return mark_safe('<img src="{}" width="250" />'.format(self.image.url))
    show_photo.short_description = 'Image Preview'
    show_photo.allow_tags = True

    class Meta:
        verbose_name_plural = '3 - Gallery'


# 4 - Exhibition Page
class Exhibition(models.Model):
    image = models.ImageField(upload_to='Portfolio/')


    def show_photo(self):
        return mark_safe('<img src="{}" width="250" />'.format(self.image.url))
    show_photo.short_description = 'Image Preview'
    show_photo.allow_tags = True

    class Meta:
        verbose_name_plural = '4 - Exhibitions'

# 5 - Social_Profile Page
class Social_Profile(models.Model):
    name = models.CharField(max_length=20)
    link = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = '5 - Social_Profile'

    def __str__(self):
        return self.name