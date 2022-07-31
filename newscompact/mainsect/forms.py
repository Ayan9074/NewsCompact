# from authentication done in a more basic way instead of using this due to time constraints, but it is also therefore less secure
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    choice1 = forms.CharField(required=True)
    choice2 = forms.CharField(required=True)
    choice3 = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password", "choice1","choice2","choice3")
    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
"""