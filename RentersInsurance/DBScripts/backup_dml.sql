INSERT INTO DeductibleFactor (Deductible, Factor) VALUES(100, '1.02');
INSERT INTO DeductibleFactor (Deductible, Factor) VALUES(250, '1');
INSERT INTO DeductibleFactor (Deductible, Factor) VALUES(500, '0.98');

INSERT INTO LiabilityBaseRate (CustomerAgeRange, BaseRate) VALUES(18, 150);
INSERT INTO LiabilityBaseRate (CustomerAgeRange, BaseRate) VALUES(26, 140);
INSERT INTO LiabilityBaseRate (CustomerAgeRange, BaseRate) VALUES(31, 130);
INSERT INTO LiabilityBaseRate (CustomerAgeRange, BaseRate) VALUES(41, 125);
INSERT INTO LiabilityBaseRate (CustomerAgeRange, BaseRate) VALUES(56, 120);
INSERT INTO LiabilityBaseRate (CustomerAgeRange, BaseRate) VALUES(70, 150);

INSERT INTO LiabilityLimitFactor (LiabilityLimit, Factor) VALUES(100000, 1);
INSERT INTO LiabilityLimitFactor (LiabilityLimit, Factor) VALUES(300000, 1.1);
INSERT INTO LiabilityLimitFactor (LiabilityLimit, Factor) VALUES(500000, 1.2);

INSERT INTO PersonalPropertyBaseRate (Territory, ConstructionType, Helper, BaseRate) VALUES(1, 'Frame', '1|Frame', 110);
INSERT INTO PersonalPropertyBaseRate (Territory, ConstructionType, Helper, BaseRate) VALUES(1, 'Brick', '1|Brick', 104);
INSERT INTO PersonalPropertyBaseRate (Territory, ConstructionType, Helper, BaseRate) VALUES(2, 'Frame', '2|Frame', 112);
INSERT INTO PersonalPropertyBaseRate (Territory, ConstructionType, Helper, BaseRate) VALUES(2, 'Brick', '2|Brick', 110);
INSERT INTO PersonalPropertyBaseRate (Territory, ConstructionType, Helper, BaseRate) VALUES(3, 'Frame', '3|Frame', 108);
INSERT INTO PersonalPropertyBaseRate (Territory, ConstructionType, Helper, BaseRate) VALUES(3, 'Brick', '3|Brick', 104);
INSERT INTO PersonalPropertyBaseRate (Territory, ConstructionType, Helper, BaseRate) VALUES(4, 'Frame', '4|Frame', 114);
INSERT INTO PersonalPropertyBaseRate (Territory, ConstructionType, Helper, BaseRate) VALUES(4, 'Brick', '4|Brick', 110);

INSERT INTO PersonalPropertyLimitFactor (LimitRange, Factor) VALUES(50000, 1);
INSERT INTO PersonalPropertyLimitFactor (LimitRange, Factor) VALUES(75000, 1.1);
INSERT INTO PersonalPropertyLimitFactor (LimitRange, Factor) VALUES(100000, 1.2);
INSERT INTO PersonalPropertyLimitFactor (LimitRange, Factor) VALUES(125000, 1.3);
INSERT INTO PersonalPropertyLimitFactor (LimitRange, Factor) VALUES(150000, 1.4);
INSERT INTO PersonalPropertyLimitFactor (LimitRange, Factor) VALUES(200000, 1.5);

INSERT INTO PolicyPlan (PolicyPlan, PolicyPlanFactor) VALUES('Preferred', 0.99);
INSERT INTO PolicyPlan (PolicyPlan, PolicyPlanFactor) VALUES('Standard', 1);

INSERT INTO CityTerritory (City, State, Territory) VALUES('Southampton', 'NY', 1);
INSERT INTO CityTerritory (City, State, Territory) VALUES('Hampton', 'NY', 2);
INSERT INTO CityTerritory (City, State, Territory) VALUES('Hoboken', 'NJ', 3);
INSERT INTO CityTerritory (City, State, Territory) VALUES('Weehawken', 'NJ', 4);
