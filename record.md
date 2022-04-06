# Init django


tasklistmng_django$ python -m venv venv

tasklistmng_django$ source venv/bin/activate

(to deactivate, run ```tasklistmng_django$ deactivate```)

to install django:
```$  python -m pip install Django```


to install django-mysql binding tool:
```$ pip install mysqlclient```


tasklistmng_django$ django-admin startproject tasklistmng

tasklistmng_django/tasklistmng$ python manage.py startapp apptasklistmng

# Change configuration

- Change databse in tasklistmng_django/tasklistmng/tasklistmng/setting.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'OPTIONS': {
            'read_default_file': str(BASE_DIR) +'/my.cnf',
        },
    }
}


TIME_ZONE = 'America/Los_Angeles' #'UTC'
```

- And create my.cnf on same path as manage.py.
```
# my.cnf
[client]
database = 'django_tasklistmng'
user = 'root'
password = 'zyj1995919'
default-character-set = utf8
```


- Create required databse on mysql:
```
mysql -u root -p 
create database django_tasklistmng;
exit
```


- Migrate default django database (tables like admin....)
tasklistmng_django/tasklistmng$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK



# Change views/urls

- Add our app in installed _apps in tasklistmng_django/tasklistmng/tasklistmng/settings.py

```
INSTALLED_APPS = [
    'apptasklistmng.apps.ApptasklistmngConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

- At this point, the django can run well.
tasklistmng_django/tasklistmng$ python manage.py runserver 8001

then open http://127.0.0.1:8001 in browser it should show the django logo.

- To use django default admin system:
$ python manage.py createsuperuser
```
Username (leave blank to use 'zhangyujie'): admin
Email address: 123@123.com
Password: admin
Password (again): 
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

Then runserver again and visit http://127.0.0.1:8001/admin in browser you can login as admin.


- Add app url into root tasklistmng_django/tasklistmng/tasklistmng/urls.py

```

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasklistmng/', include(apptasklistmng.urls)),
]
```

- Create and Add url in app tasklistmng_django/tasklistmng/apptasklistmng/urls.py
```
from django.urls import path

from . import views

appname = "tasklistmng"

urlpatterns = [
    path('', views.index, name='index'),
]
```

- Add first index view in tasklistmng_django/tasklistmng/apptasklistmng/views.py

```
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

- Create tasklistmng_django/tasklistmng/apptasklistmng/templates/apptasklistmng/index.html

- Change index view to 
```
def index(request):
    return render(request, "apptasklistmng/index.html")
```
at this momement, we can see taskslist in http://127.0.0.1:8000/tasklistmng/ 


- Add css file
   - add static in tasklisting_django/tasklistmng/apptasklistmng/static
   - then add apptasklistmng in tasklisting_django/tasklistmng/apptasklistmng/static, then add style.css in tasklisting_django/tasklistmng/apptasklistmng/static/apptasklistmng.
  - then add 
```
{% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'apptasklistmng/style.css' %}">

``` 
in template/apptasklistmng/index.html

- Add js file
  - create taskListScript.js under templates/apptasklistmng
  - add Task.js under templates/apptasklistmng
  - add 

```
<script src="{% static 'apptasklistmng/tasksListScript.js' %}"></script>
```
 in template/apptasklistmng/index.html

- add signin.html, signon.html,in tasklisting_django/tasklistmng/apptasklistmng/template/apptasklistmng 

- signin.js and signon.js in tasklisting_django/tasklistmng/apptasklistmng/static/apptasklistmng/scripts
- change related file path. 

# Our Database

- Create database by hand:
tasklistmng_django/tasklistmng(master✗)(system: ruby 2.6.3p62) ]$ mysql -u root -p < databasesetup/setupdb.sql
```
Enter password: 
Tables_in_django_tasklistmng
Tasks
UserChangeRecords
UserLoginActivityRecords
Users
userno	userfirname	usermidname	userlasname	usernickname	useremail	usergender	userpwd	userdob	usernote1	usernote2
1	testfirname	testmidname	testlasname	testnickname	testuseremail	female	testpwd	2022-04-04	1	testnote2
```



- Use inspectdb tool to convert our databses to django models. It generates apptasklistmng/models.py for us.

/tasklistmng_django/tasklistmng(master✗)(system: ruby 2.6.3p62) ]$ python manage.py inspectdb > apptasklistmng/models.py


- Change the "managed = False" to "true". The  deault value is true so we can comment it.
  


- To check it works well with database
```
tasklistmng_django/tasklistmng(master✗)(system: ruby 2.6.3p62) ]
 $ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK


(venv) (base) [  9:26PM ]  [ zhangyujie@zhangdeMacBook-Pro:~/Desktop/projects/tasklistmng_django/tasklistmng(master✗)(system: ruby 2.6.3p62) ]
 $ python manage.py shell          
Python 3.8.8 (default, Apr 13 2021, 12:59:45) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from apptasklistmng.models import Users
>>> Users.objects.all()
<QuerySet [<Users: Users object (1)>]>
>>> Users.objects.filter(pk=1)
<QuerySet [<Users: Users object (1)>]>
```


# Djaango form

- signin.html <form> set action  to destination page. Don't forget {% csrf_token %}  it used for any cross page/view data tranmission in django. 
```
<form  action="{% url 'signinprocess'  %}" method="POST"> 
{% csrf_token %}  
</form>
```

- create forms.py and its class SignInForm 

- add 'signinprocess/' path in usrls.py
- add 'signinprocess' view in views.py
```py
def signinprocess(request):
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


            # redirect to a new URL:
            return render(request, "apptasklistmng/userprofile.html", {"usernickname": usernickname, "userpwd": userpwd})
        return HttpResponse("hello signin process invalid")

    # if a GET (or any other method) we'll create a blank form
    else:
        return HttpResponse("hello signin process don't use get")
```


- Attention: The "name" in html input tag/element must  be same as the modle file "forms.py" vairbale name.