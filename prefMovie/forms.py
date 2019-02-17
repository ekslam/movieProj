from django.forms import ModelForm
from .models import Movies, Users

class MovieModuleForm(ModelForm):
    class Meta:
        model = Movies
        exclude = ['id']

class UsersModuleForm(ModelForm):
    class Meta:
        model = Users
        exclude = ['id']