from django import forms
from django.contrib.auth import get_user_model, authenticate, login, logout 
from .models import Content, Answer

class Answerform(forms.ModelForm):

    class Meta:
        
        model = Answer
        fields =('subject', 'topic','answer',)

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        checkusername = get_user_model().objects.filter(username=username)
        if checkusername.exists():
            raise forms.ValidationError('username exists')

        checkemail = get_user_model().objects.filter(email=email)
        if checkemail.exists():
            raise forms.ValidationError('email exists')

        return super(UserRegisterForm, self).clean(*args, **kwargs)

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)    
        
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('invalid login details')
        return super(UserLoginForm, self).clean(*args, **kwargs)
