# Init django

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
