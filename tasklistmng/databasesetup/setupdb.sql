DROP DATABASE IF EXISTS django_tasklistmng;

create database django_tasklistmng;
use django_tasklistmng;
create table Users
(	userno	 		int not null auto_increment,
	userfirname	 	varchar(20) not null,
    usermidname	 	varchar(20),
	userlasname 	varchar(20) not null,
    usernickname	varchar(20) not null,
    useremail		varchar(30) not null,
    usergender		varchar(6) not null,
	userpwd			varchar(30) Not Null,
	userdob     	date not null,
	usernote1		int,
	usernote2		varchar(30),
    Constraint UsersPK Primary key (userno),
    Constraint Uniqueusernn	Unique(usernickname));

    
create table Tasks(
	taskno				int not null auto_increment,
    taskcontent			varchar(100) not null,
    taskddl				date not null,
    taskorder			int not null,
    taskisimportant		boolean not null,
    taskisfinished		boolean not null,
    userno				int not null,
    Constraint TasksPK Primary key (taskno),
    CONSTRAINT TasksFK FOREIGN KEY (userno) REFERENCES Users (userno)
);

create table UserChangeRecords (
	chgno			int not null auto_increment,
	chgtime 		datetime not null,
	chgentry		varchar(100),
	chgbefore		varchar(100),
	chgafter		varchar(100),
	chgpwd			varchar(30),
	chgpwdbefore	varchar(30),
	chgpwdafter		varchar(30),
    userno			int not null,
    Constraint UserChangeRecordsPK Primary key (chgno),
	CONSTRAINT UserChangeRecordsFK FOREIGN KEY (userno) REFERENCES Users (userno)
);

create table UserLoginActivityRecords (
	actno		int not null auto_increment,
	acttime		datetime not null,
	acttype		varchar(10),
    userno 		int not null,
    Constraint UserLoginActivityRecordsPK Primary key (actno),
    CONSTRAINT UserLoginActivityRecordsFK FOREIGN KEY (userno) REFERENCES Users (userno)
);
show tables;

insert Users
values(	
Null, 	-- userno	 		int not null auto_increment,
"testfirname", -- 	userfirname	 	varchar(20) not null,
"testmidname", --     usermidname	 	varchar(20),
"testlasname", -- 	userlasname 	varchar(20) not null,
"testnickname", --     usernickname	varchar(20) not null,
"testuseremail", --     useremail		varchar(30) not null,
"female", --     usergender		varchar(6) not null,
"testpwd", -- 	userpwd			varchar(30) Not Null,
CURDATE(), -- 	userdob     	date not null,
1, -- 	usernote1		int,
"testnote2" -- 	usernote2		varchar(30),
);

select * from users;
