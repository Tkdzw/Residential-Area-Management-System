#State Database Name and Select It
CREATE SCHEMA `lupane` ;
USE `lupane`;

##############################################################
#Tables

CREATE TABLE residents (
	AccNumber	INTEGER NOT NULL AUTO_INCREMENT,
	Firstname	VARCHAR(12) NOT NULL,
	Surname		VARCHAR(12) NOT NULL,
	ID_Number	VARCHAR(15) NOT NULL,
	Date_OB	DATE NOT NULL,
	Address	VARCHAR(45) DEFAULT NULL ,
	RegistrationDate	DATE NOT NULL,
	Phone	VARCHAR(12),
	PRIMARY KEY(AccNumber)
);

CREATE TABLE land (
	StandNumber	INT NOT NULL AUTO_INCREMENT,
	LandSize 	INT NOT NULL,
	LandLocation	VARCHAR(15) NOT NULL,
	Status	VARCHAR(15) DEFAULT NULL,
	Price	INT DEFAULT NULL,
	PRIMARY KEY(StandNumber)
);

CREATE TABLE payments (
	PaymentID	INTEGER NOT NULL AUTO_INCREMENT,
	AccountNumber	INT NOT NULL,
	MeterNumber	VARCHAR(15) NOT NULL,
	PaymentMethod	VARCHAR(12) NOT NULL,
	PaymentDate	DATE NOT NULL,
	Amount	VARCHAR(45) NOT NULL,
	PRIMARY KEY(PaymentID )
);

CREATE TABLE employees (
	EmployeesNumber	INT NOT NULL AUTO_INCREMENT,
	Name	VARCHAR(12) NOT NULL,
	Surname	VARCHAR(15) NOT NULL,
	ID_Number	VARCHAR(8) NOT NULL,
	Title	VARCHAR(10) NOT NULL,
	Date_Joined	DATE NOT NULL,
	PRIMARY KEY(EmployeesNumber)
);

CREATE TABLE billings (
	BillNumber INT NOT NULL auto_increment,
	MeterNumber INT NOT NULL,
     MeterReadings INT NOT NULL, 
     AmountDue INT NOT NULL, 
     BillDate DATE NOT NULL,
     PRIMARY KEY(BillNumber)
);

CREATE TABLE auth (
	ID	INTEGER NOT NULL AUTO_INCREMENT,
	Username	VARCHAR(25) NOT NULL,
	Password	VARCHAR(15) NOT NULL,
	PRIMARY KEY(ID)
);

CREATE TABLE meteraccount (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `MeterNumber` VARCHAR(45) NOT NULL,
  `AccountNumber` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`));

##############################################################

#Views
#Bill Totals
CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `billtotals` AS
    SELECT 
        `b`.`BillNumber` AS `BillNumber`,
        `b`.`MeterNumber` AS `MeterNumber`,
        SUM(`b`.`AmountDue`) AS `Amount Due`
    FROM
        `billings` `b`
    GROUP BY `b`.`MeterNumber`;

#PaymentTotals
    CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `paymenttotals` AS
    SELECT 
        `p`.`AccountNumber` AS `AccountNumber`,
        `p`.`MeterNumber` AS `MeterNumber`,
        SUM(`p`.`Amount`) AS `Amount Paid`
    FROM
        `payments` `p`
    GROUP BY `p`.`MeterNumber`;
    
#Account Balances
    CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `accountbalances` AS
    SELECT 
        `b`.`BillNumber` AS `BillNumber`,
        `b`.`MeterNumber` AS `MeterNumber`,
        `p`.`AccountNumber` AS `AccountNumber`,
        (`b`.`Amount Due` - `p`.`Amount Paid`) AS `Balance`
    FROM
        (`billtotals` `b`
        JOIN `paymenttotals` `p` ON ((`b`.`MeterNumber` = `p`.`MeterNumber`)));
        
#Bills 
    CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `bills` AS
    SELECT 
        `b`.`BillNumber` AS `BillNumber`,
        `b`.`MeterNumber` AS `MeterNumber`,
        `m`.`AccountNumber` AS `AccountNumber`,
        `r`.`Firstname` AS `Firstname`,
        `r`.`Surname` AS `Surname`,
        `r`.`Address` AS `Address`,
        `b`.`BillDate` AS `BillDate`,
        `b`.`MeterReadings` AS `MeterReadings`,
        `b`.`AmountDue` AS `AmountDue`
    FROM
        ((`billings` `b`
        JOIN `meteraccount` `m` ON ((`b`.`MeterNumber` = `m`.`MeterNumber`)))
        JOIN `residents` `r` ON ((`r`.`AccNumber` = `m`.`AccountNumber`)));
        
#pays
	CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `pays` AS
    SELECT 
        `p`.`PaymentID` AS `PaymentNumber`,
        `p`.`MeterNumber` AS `MeterNumber`,
        `p`.`AccountNumber` AS `AccountNumber`,
        `r`.`Firstname` AS `Firstname`,
        `r`.`Surname` AS `Surname`,
        `r`.`Address` AS `Address`,
        `p`.`PaymentDate` AS `PaymentDate`,
        `p`.`Amount` AS `Amount`
    FROM
        (`payments` `p`
        JOIN `residents` `r` ON ((`p`.`AccountNumber` = `r`.`AccNumber`)));
        
	#Database Sample Data
    
    INSERT INTO `auth` (`ID`, `Username`, `Password`) VALUES ('1111', 'Tkdzw', '1111');

CREATE SCHEMA IF NOT EXISTS `councils` ;

CREATE TABLE `councils`.`connectdb` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Council` VARCHAR(45) NULL,
  PRIMARY KEY (`ID`));
