import hashlib
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.http import HttpResponse

from .forms import SignInForm
from .forms import SignOnForm
from .models import Users, Tasks, Userchangerecords, Userloginactivityrecords


def index(request):
    return render(request, "apptasklistmng/index.html")

def indexLongerUrl(request):
    return redirect('apptasklistmng:index')

def signin(request):
    return render(request, "apptasklistmng/signin.html")

def signinLongerUrl(request):
    return redirect('apptasklistmng:signin')

def signon(request):
    return render(request, "apptasklistmng/signon.html")

def signonLongerUrl(request):
    return redirect('apptasklistmng:signon')

def signinprocess(request):
    # return HttpResponse("hello signin  process")

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignInForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            form.cleaned_data # convert it to dict
            usernickname = form["usernickname"].value()
            userpwd = form["userpwd"].value()
            print("usernickname: ", usernickname)
            print("userpwd: ", userpwd)
            userpwd = str(hashlib.md5( userpwd.encode() ).hexdigest() )
            print("userpwd hash: ", userpwd)

            # connect DB
            try:
                user = Users.objects.get(usernickname=usernickname, userpwd=userpwd)
            except Users.DoesNotExist:
                return render(request, "apptasklistmng/signin.html", {"errormsg": "Username or Password Incorrect."})
            return render(request, "apptasklistmng/userprofile.html", {"usernickname": usernickname, "userpwd": userpwd})
           
        return render(request, "apptasklistmng/wrong.html", {"errormsg": "hello signin process invalid."})

    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, "apptasklistmng/wrong.html", {"errormsg": "hello signin process don't use get."})

    

def signonprocess(request):
    if request.method == 'POST':
        form = SignOnForm(request.POST)
        if form.is_valid():
            form.cleaned_data 
            userfirstname = form["userfirstname"].value()
            usermiddlename = form["usermiddlename"].value()
            userlastname = form["userlastname"].value()
            useremail = form["useremail"].value()
            userdob = form["userdob"].value()
            usergender = form["usergender"].value()
            usernickname = form["usernickname"].value()
            userpwd = form["userpwd"].value()
            print("usernickname: ", usernickname)
            print("userlastname: ", userlastname)
            print("userfirstname: ", userfirstname)
            print("usermiddlename: ", usermiddlename)
            print("useremail: ", useremail)
            print("usedob: ", userdob)
            print("usergender: ", usergender)
            print("userpwd: ", userpwd)
            userpwd = str(hashlib.md5( userpwd.encode() ).hexdigest())
            print("userpwd hash: ", userpwd)

            # connect Db
            #  Users.objects.create(userfirname="testfirname2", userlasname="testlasname2", 
            #  usernickname="testnickname2", useremail="test@test.test", 
            #  usergender="female", userpwd="testpwdA1", userdob="2022-04-06")
            try:
                Users.objects.create(userfirname=userfirstname, usermidname=usermiddlename, userlasname=userlastname, 
                usernickname=usernickname, useremail=useremail, 
                usergender=usergender, userpwd=userpwd, userdob=userdob)
            except:
                return render(request, "apptasklistmng/signon.html", {"errormsg": "Username or Password Incorrect."})
            return render(request, "apptasklistmng/userprofile.html", {"usernickname": usernickname, "userpwd": userpwd, "userlastname: ": userlastname, "userfirstname: ": userfirstname,"usermiddlename: ": usermiddlename, "useremail: ": useremail,"usedob: ": userdob, "usergender: ":usergender })
        return render(request, "apptasklistmng/wrong.html", {"errormsg": "hello signon process invalid."})        
    else:
        return render(request, "apptasklistmng/wrong.html", {"errormsg": "hello signon process don't use get."})  
      