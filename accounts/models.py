from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify


GENDER = (
    ('M', 'Male'),
    ('F', 'Female')
)

class Profile(models.Model):

    Specialite = (
    ('Pediatre', 'Pediatre'),
    ('Medecin general', 'Medecin general'),
    ('Chirugien', 'Chirugien'),
    
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField("Se tour",max_length=50)
    who_i = models.TextField("Yay kane")
    price = models.IntegerField(blank=True,null=True)
    image = models.ImageField('Se photo',upload_to='profils',blank=True,null=True)
    slug = models.SlugField("slug", blank=True,null=True)
    Specialist_doctor = models.CharField("Specialite",max_length=100 , choices=Specialite, blank=True, null=True)
    Address = models.CharField("Votre adresse",max_length=100,blank=True, null=True)
    number_phone = models.CharField("Votre numeros de telephone",max_length=50,blank=True, null=True)
    working_hours = models.IntegerField("Heur de travail", blank=True, null=True)
    subtitle = models.CharField(max_length=80,blank=True,null=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twiter = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    google_plus = models.CharField(max_length=100, null=True, blank=True)
    join_new = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    gender = models.CharField(max_length=100,choices=GENDER)

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