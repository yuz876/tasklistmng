from django import forms

class SignInForm(forms.Form):
    usernickname = forms.CharField(label='Username', max_length=20)
    userpwd = forms.CharField(label='Password', max_length=30)

class SignOnForm(forms.Form):
    userfirstname = forms.CharField(label='firstname', max_length=20)
    usermiddlename = forms.CharField(label='middlename', max_length=20)
    userlastname = forms.CharField(label='lastname', max_length=20)
    usernickname = forms.CharField(label='username', max_length=20)
    useremail = forms.CharField(label='email', max_length=30)
    userdob = forms.DateField(label='dob')
    usergender = forms.CharField(label='gender', max_length=6)
    userpwd = forms.CharField(label='password', max_length=30)

#     kkk
# <QueryDict: {'csrfmiddlewaretoken': ['KuUcXeqWMnGKQtMJPr4Tot63nVlzpLY1YUcdELdDbnDvkv7tdVfrkrKGPvKMXoEV'], 
# 'firstname': ['q'], 'middlename': ['q'], 'lastname': ['q'], 'username': ['q'], 'password': ['Aa123456'],
#  'email': ['a@1.c'], 'gender': ['male'], 'dob': ['']}>