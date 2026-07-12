from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


#注册表单
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='密码')
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='确认密码')
    class Meta:
        model = User
        fields = ['username','email','password',]
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
        labels={
            'username':'用户名',
            'email':'邮箱'
        }
        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            password_confirm = cleaned_data.get('password_confirm')
            if password != password_confirm:
                raise forms.ValidationError('两次密码输入不一致')
            return cleaned_data


    #登录表单
class LoginForm(AuthenticationForm):
        username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='用户名')
        password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='密码')