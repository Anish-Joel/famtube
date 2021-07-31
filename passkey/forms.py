from django import forms
from django.contrib.auth import get_user_model


# check for unique email & username

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(
       label='passkey' )
    password = forms.CharField(label='passkey password ',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('full_name', 'email',) #'full_name',)

        
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        # user.active = False # send confirmation email
        if commit:
            user.save()
        return user


  #  def clean_username(self):
     #  please  = self.cleaned_data.get("passkey")
      # qs = User.objects.filter(username__iexact=username)

      # if qs.exists():
     #      raise forms.ValidationError("This is an invalid passkey, please pick another.")
     #  return passkey
    
   


class LoginForm(forms.Form):
    username= forms.CharField(label='passkey',widget=forms.TextInput)
    password = forms.CharField(label='passkey password',widget=forms.PasswordInput)
   # def clean_username(self):
     #   username = self.cleaned_data('username')
     #   qs = User.objects.filter(username__iexact#=passkey
        
     #   ) # thisIsMyUsername == thisismyusername
     #   if not qs.exists():
      #      raise forms.ValidationError("This is an  #passkey.")
        
     #  return username