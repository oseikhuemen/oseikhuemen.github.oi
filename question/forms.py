from django import forms
from .models import Question


class Maskform(forms.ModelForm):

    class Meta:
        
        model = Question
        fields =('name', 'email', 'subject', 'topic', 'question')