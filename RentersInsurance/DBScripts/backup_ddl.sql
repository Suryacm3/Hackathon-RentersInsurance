CREATE TABLE `DeductibleFactor` (
  `Deductible` int(11) NOT NULL,
  `Factor` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `LiabilityBaseRate` (
  `CustomerAgeRange` int(11) DEFAULT NULL,
  `BaseRate` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `LiabilityLimitFactor` (
  `LiabilityLimit` int(11) DEFAULT NULL,
  `Factor` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `PersonalPropertyBaseRate` (
  `Territory` int(11) NOT NULL,
  `ConstructionType` varchar(100) NOT NULL,
  `Helper` varchar(100) NOT NULL,
  `BaseRate` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `PersonalPropertyLimitFactor` (
  `LimitRange` int(11) DEFAULT NULL,
  `Factor` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `PolicyPlan` (
  `PolicyPlan` varchar(100) DEFAULT NULL,
  `PolicyPlanFactor` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `CityTerritory` (
  `City` varchar(100) NOT NULL,
  `State` varchar(10) NOT NULL,
  `Territory` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `QuoteHistory` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `InsuranceType` varchar(100) DEFAULT NULL,
  `PolicyStartDate` varchar(15) DEFAULT NULL,
  `FirstName` varchar(100) DEFAULT NULL,
  `LastName` varchar(100) DEFAULT NULL,
  `EmailAddress` varchar(100) DEFAULT NULL,
  `PhoneNumber` varchar(100) DEFAULT NULL,
  `AddressLine1` varchar(255) DEFAULT NULL,
  `AddressLine2` varchar(200) DEFAULT NULL,
  `City` varchar(100) DEFAULT NULL,
  `State` varchar(100) DEFAULT NULL,
  `Zip` varchar(15) DEFAULT NULL,
  `Plan` varchar(10) DEFAULT NULL,
  `PPCoveragevalue` int(11) DEFAULT NULL,
  `BuildingType` varchar(10) DEFAULT NULL,
  `Deductible` int(11) DEFAULT NULL,
  `LCoverageValue` int(11) DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `PersonalPremium` double DEFAULT NULL,
  `LiabilityPremium` double DEFAULT NULL,
  `TotalPremium` double DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=latin1;