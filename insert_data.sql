INSERT INTO process_manager_customer (DocumentType, DocumentNumber)
VALUES ('ID', '000000001');

INSERT INTO process_manager_applicationstatus ("StatusDescription", "CreationDate", "ModificationDate")
VALUES ('Offer', NOW(), NOW());

INSERT INTO process_manager_application ("CreationDate", "ModificationDate", "CustomerID_id", "StatusID_id")
VALUES (NOW(), NOW(), 1, 1);

INSERT INTO process_manager_basicinformation ("ApplicationID_id", "FirstName", "LastName", "Country", "State", "City", "MobileNumber", "Email", "CreationDate", "ModificationDate")
VALUES (1, 'John', 'Doe', 'CountryX', 'StateY', 'CityZ', '1234567890', 'john.doe@example.com', NOW(), NOW());

INSERT INTO process_manager_economicinformation ("ApplicationID_id", "Profession", "EconomicActivity", "CompanyName", "PositionInCompany", "CompanyContact", "Income", "Expenses", "Assets", "Liabilities", "NetWorth", "FullAddress", "CreationDate", "ModificationDate")
VALUES (1, 'Software Developer', 'Software', 'Company Inc.', 'Senior Developer', '123-456-7890', 5000, 2000, 15000, 5000, 10000, '123 Main St, CityZ, StateY, CountryX', NOW(), NOW());

