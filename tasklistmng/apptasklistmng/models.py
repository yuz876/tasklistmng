# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Users(models.Model):
    userno = models.AutoField(primary_key=True)
    userfirname = models.CharField(max_length=20)
    usermidname = models.CharField(max_length=20, blank=True, null=True)
    userlasname = models.CharField(max_length=20)
    usernickname = models.CharField(unique=True, max_length=20)
    useremail = models.CharField(max_length=30)
    usergender = models.CharField(max_length=6)
    userpwd = models.CharField(max_length=30)
    userdob = models.DateField()
    usernote1 = models.IntegerField(blank=True, null=True)
    usernote2 = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'Users'


class Tasks(models.Model):
    taskno = models.AutoField(primary_key=True)
    taskcontent = models.CharField(max_length=100)
    taskddl = models.DateField()
    taskorder = models.IntegerField()
    taskisimportant = models.IntegerField()
    taskisfinished = models.IntegerField()
    userno = models.ForeignKey('Users', models.DO_NOTHING, db_column='userno')

    class Meta:
        # managed = False
        db_table = 'Tasks'


class Userchangerecords(models.Model):
    chgno = models.AutoField(primary_key=True)
    chgtime = models.DateTimeField()
    chgentry = models.CharField(max_length=100, blank=True, null=True)
    chgbefore = models.CharField(max_length=100, blank=True, null=True)
    chgafter = models.CharField(max_length=100, blank=True, null=True)
    chgpwd = models.CharField(max_length=30, blank=True, null=True)
    chgpwdbefore = models.CharField(max_length=30, blank=True, null=True)
    chgpwdafter = models.CharField(max_length=30, blank=True, null=True)
    userno = models.ForeignKey('Users', models.DO_NOTHING, db_column='userno')

    class Meta:
        # managed = False
        db_table = 'UserChangeRecords'


class Userloginactivityrecords(models.Model):
    actno = models.AutoField(primary_key=True)
    acttime = models.DateTimeField()
    acttype = models.CharField(max_length=10, blank=True, null=True)
    userno = models.ForeignKey('Users', models.DO_NOTHING, db_column='userno')

    class Meta:
        # managed = False
        db_table = 'UserLoginActivityRecords'

