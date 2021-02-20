from django.db import models


class SignUp(models.Model):

	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	email = models.EmailField(max_length=254)
	password = models.CharField(max_length=100)

	USERNAME_FIELD = 'email'