from django.shortcuts import render
from .serializers import SignUpSerializer, LoginSerializer
from django.contrib.auth import login, authenticate
from .models import SignUp
from rest_framework import status
from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.

def home(request):
	return render(request, 'home.html')


def login(request):
	return render(request, 'login.html')


def signup(request):
	return render(request, 'signup.html')


def retrieve(request):
	return render(request, 'retrieve.html')

def update(request):
	return render(request, 'update.html')


def delete(request):
	return render(request, 'delete.html')


@method_decorator(csrf_exempt, name='dispatch')
class UserView(CreateAPIView):
	queryset = SignUp.objects.all()
	serializer_class = SignUpSerializer


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(GenericAPIView):
	queryset = SignUp.objects.all()
	serializer_class = LoginSerializer

	def post(self, request, *args, **kwargs):
		serializer_class = LoginSerializer(data=request.data)
		if serializer_class.is_valid(raise_exception=True):
			return render(request, 'success.html')
			# return Response(serializer_class.data, status=status.HTTP_200_OK)

		return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveView(RetrieveAPIView):
	queryset = SignUp.objects.all()
	serializer_class = SignUpSerializer



class UpdateView(UpdateAPIView):
	queryset = SignUp.objects.all()
	serializer_class = SignUpSerializer



class DeleteView(DestroyAPIView):
	queryset = SignUp.objects.all()
	serializer_class = SignUpSerializer
