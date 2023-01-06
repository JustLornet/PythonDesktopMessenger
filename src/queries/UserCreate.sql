use PythonMessenger

create table Users 
(
	UserID int primary key identity,
	Login nvarchar(50) unique not null default 'undefined',
	LastOnline datetime null,
	RegistrationDatetime datetime null,
	IsOnline bit not null default 0
)