from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField("Se tour",max_length=50)
    who_i = models.TextField("Yay kane")
    price = models.IntegerField(blank=True,null=True)
    image = models.ImageField('Se photo',upload_to='profils',blank=True,null=True)
    slug = models.SlugField("slug", blank=True,null=True)

    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile,self).save(*args,**kwargs)



    def __str__(self):
        return '%s' %(self.user.username)


def create_profile(sender,**kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)