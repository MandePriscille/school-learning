from django.db import models
from django.contrib.auth.models import User


# def renomer_imager(instance, filename):
#     upload_to = '/image/'
#     ext = filename.split('.'){-1}

class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # bio = models.CharField(max_length=150, blank=True)
    # photo_profile = models.ImageField(upload_to='/images')

    # etudiant = 'etudiant',
    # enseignant = 'enseignant'
    # parent = 'parent'

    # type_user = [
    #     (etudiant, 'etudiant'),
    #     (enseignant, 'enseignant'),
    #     (parent, 'parent')
    # ]

    # type_profile = models.CharField(max_length=100, choices=type_user, default=etudiant)
    pass