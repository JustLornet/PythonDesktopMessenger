use PythonMessenger

create table Messages 
(
	MessageID int primary key identity,
	Message nvarchar(MAX),
	SendTime datetime null,
	SenderID int REFERENCES Users (UserID),
	AddresseeID int REFERENCES Users (UserID),
)