from django.db import models
from django.template.defaultfilters import slugify

# from users.models import User
from django.contrib.auth.models import User


class Niveaux(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.nom
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super().save(*args, **kwargs)



class Matiere(models.Model):
    matiere_id = models.CharField(max_length=30, unique=True)
    nom = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    niveau = models.ForeignKey(Niveaux, on_delete=models.CASCADE, related_name='matiere')
    image = models.ImageField(upload_to='matiere', blank=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.nom
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super().save(*args, **kwargs)
    

class Lesson(models.Model):
    lesson_id = models.CharField(unique=True)
    niveau = models.ForeignKey(Niveaux, on_delete=models.CASCADE)
    creer_par = models.ForeignKey(User,on_delete=models.CASCADE )
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name="lesson")
    nom = models.CharField(max_length=100)
    position = models.PositiveSmallIntegerField(verbose_name="chapitre numero")
    video = models.FileField(upload_to="video", null=True, blank=True)
    fichier = models.FileField(upload_to="files", null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nom
    
    class Meta:
        ordering = ['position']


