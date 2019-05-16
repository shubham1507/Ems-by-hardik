from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model =  User
        fields = ['first_name','last_name',
            'email','username',
        'password']

        label = {
           'password':'Password' 
        }

        # def clean_email(self):
        #     if self.cleaned_data['email'].endsWith('@gmail.com')

        #     else:
        #         raise ValidationError("EmailId isnt valid")

    def save(self):

        password = self.cleaned_data.pop('password')

        u = super.save()
        u.set_password(password)
        u.save()

        