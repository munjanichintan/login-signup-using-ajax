from django.contrib import admin
from .models import SignUp

# Register your models here.
@admin.register(SignUp)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'email')
