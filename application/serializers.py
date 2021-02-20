from .models import SignUp
from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.db.models import Q 

class SignUpSerializer(serializers.ModelSerializer):
	class Meta:
		model = SignUp
		fields = ['id', 'firstname', 'lastname', 'email', 'password']


class LoginSerializer(serializers.ModelSerializer):
	def validate(self, data):
		email = data.get('email', None)
		password = data.get('password', None)
		user = None
		user = SignUp.objects.filter(Q(email=email) & Q(password=password))
		if not user.exists():
			raise ValidationError("User credential are not correct")
		user = SignUp.objects.get(email=email)
		user.save()
		return data

	class Meta:
		model = SignUp
		fields = ['email', 'password']