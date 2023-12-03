from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

class CustomSignupForm(SignupForm):

    def save(self, request):
        user = super().save(request)
        readers = Group.objects.get(name='readers')
        user.groups.add(readers)
        return user
