from django import forms

class SignInForm(forms.Form):
    usernickname = forms.CharField(label='Username', max_length=20)
    userpwd = forms.CharField(label='Password', max_length=30)

class SignOnForm(forms.Form):
    GENDER_CHOICES =  [
        ("notsay", 'Gender'),
        ("male", 'Male'),
        ("female", 'Female'),
        ("other", 'Other'),
    ] 
    userfirstname = forms.CharField(label='firstname', max_length=20)
    usermiddlename = forms.CharField(label='middlename', max_length=20, required=False)
    userlastname = forms.CharField(label='lastname', max_length=20)
    usernickname = forms.CharField(label='username', max_length=20)
    useremail = forms.CharField(label='email', max_length=30)
    userdob = forms.DateField(label='dob')
    usergender = forms.ChoiceField(label='gender', choices=GENDER_CHOICES)
    userpwd = forms.CharField(label='password', max_length=30)
