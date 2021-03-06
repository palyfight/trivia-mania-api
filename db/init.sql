CREATE DATABASE trivia;
use trivia;

CREATE TABLE user (
  ID INT AUTO_INCREMENT PRIMARY KEY,
  UserName VARCHAR(255) NOT NULL,
  Email VARCHAR(255) NOT NULL,
  Password VARCHAR(255) NOT NULL,
  TotalScore SMALLINT,
  BestScore SMALLINT,
  LastPlayDate DATE,
  CONSTRAINT UC_Person UNIQUE(ID, UserName, Email)
);

CREATE TABLE category (
	ID INT AUTO_INCREMENT PRIMARY KEY,
	Name VARCHAR(255) NOT NULL
);

CREATE TABLE question (
	ID INT AUTO_INCREMENT PRIMARY KEY,
	Description VARCHAR(255) NOT NULL,
	-- tf: true/false, mc: multiple choice, sa: short answer
	Type ENUM('tf', 'mc', 'sa'),
	ChoiceA VARCHAR(255),
	ChoiceB VARCHAR(255),
	ChoiceC VARCHAR(255),
	ChoiceD VARCHAR(255),
	Answer VARCHAR(255) NOT NULL,
	CategoryID INT NOT NULL,
	Difficulty VARCHAR(255) NOT NULL,
	Points INT NOT NULL,
	FOREIGN KEY (CategoryID) REFERENCES category(ID)
);

CREATE TABLE leaderboard (
	ID INT AUTO_INCREMENT PRIMARY KEY,
	UserID INT NOT NULL,
	CategoryID INT NOT NULL,
	Score SMALLINT,
	DateOfPlay DATE,
	FOREIGN KEY (UserID) REFERENCES user(ID),
	FOREIGN KEY (CategoryID) REFERENCES category(ID)
);