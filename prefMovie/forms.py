from django.forms import ModelForm
from .models import Movies, Comment
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput

class MovieModuleForm(ModelForm):
    class Meta:
        model = Movies
        exclude = ['id']

class RegistrationModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': PasswordInput()
        }


class CommentModelForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['id']