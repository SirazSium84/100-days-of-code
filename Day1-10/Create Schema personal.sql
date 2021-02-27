Create Schema test_case_2;
CREATE TABLE test_case_2.person (
	ID int,
	Name VARCHAR (20),
	Home VARCHAR (30),
	Age int ,
	Occupation VARCHAR (45),
	Gender VARCHAR (6),
	Salary int,
    PRIMARY KEY (ID)
);

CREATE TABLE test_case_2.Phone (
    ID int,
    brand varchar(40),
    model varchar(49),
    screensize int
    );



INSERT INTO test_case_2.person VALUES (1, 'Maisha', 'Dhaka', 25, 'Teacher', 'Female', 50000);
INSERT INTO test_case_2.person VALUES (2, 'Saad', 'Dhaka', 56, 'Service', 'Male', 60000);
INSERT INTO test_case_2.person VALUES (3, 'Rakeen', 'Ctg', 71, 'Retired', 'Male', 10000);
INSERT INTO test_case_2.person VALUES (6, 'Ilma', 'Gazipur', 54, 'Doctor', 'Female', 55000);
INSERT INTO test_case_2.person VALUES (7, 'Rajib', 'Gazipur', 65, 'Musician', 'Male', 5000);
INSERT INTO test_case_2.person VALUES (8, 'Raisa', 'Dhaka', 56, 'Engineer', 'Female', 60000);
INSERT INTO test_case_2.person VALUES (9, 'Sakib', 'Ctg', 23, 'Student', 'Male', 1000);
INSERT INTO test_case_2.person VALUES (10, 'Mosaddek', 'Comilla', 32, 'Teacher', 'Male', 45000);
INSERT INTO test_case_2.person VALUES (11, 'Jarin', 'Comilla', 51, 'Farmer', 'Female', 20000);
INSERT INTO test_case_2.person VALUES (12, 'Rudaba', 'Khulna', 15, 'Student', 'Female', 1500);
INSERT INTO test_case_2.person VALUES (13, 'Sami', 'Ctg', 25, 'Business', 'Male', 100000);
INSERT INTO test_case_2.person VALUES (14, 'Nihal', 'Comilla', 52, 'Doctor', 'Male', 70000);
INSERT INTO test_case_2.person VALUES (15, 'Rafid', 'Gazipur', 53, 'Teacher', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (16, 'Medha', 'Dhaka', 35, 'Musician', 'Female', 50000);
INSERT INTO test_case_2.person VALUES (17, 'Sakib', 'Khulna', 43, 'Service', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (18, 'Zobaeir', 'Khulna', 34, 'Service', 'Male', 45000);
INSERT INTO test_case_2.person VALUES (19, 'Shahriyar', 'Ctg', 16, 'Student', 'Male', 500);
INSERT INTO test_case_2.person VALUES (20, 'Mahir', 'Comilla', 32, 'Business', 'Male', 120000);
INSERT INTO test_case_2.person VALUES (21, 'Mushfiqur', 'Ctg', 25, 'Musician', 'Male', 100000);
INSERT INTO test_case_2.person VALUES (22, 'Najish', 'Gazipur', 14, 'Student', 'Male', 400);
INSERT INTO test_case_2.person VALUES (23, 'Bandhan', 'Dhaka', 25, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (24, 'Shadman', 'Ctg', 28, 'Teacher', 'Male', 80000);
INSERT INTO test_case_2.person VALUES (25, 'Faria', 'Dhaka', 25, 'Engineer', 'Female', 50000);
INSERT INTO test_case_2.person VALUES (26, 'Taki', 'Dhaka', 26, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (27, 'Tanzir', 'Dhaka', 45, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (28, 'Alvi', 'Ctg', 23, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (29, 'Nasib', 'Dhaka', 21, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (30, 'Mim', 'Dhaka', 75, 'Teacher', 'Female', 40000);
INSERT INTO test_case_2.person VALUES (31, 'Ornob', 'Dhaka', 43, 'Student', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (32, 'Shuvo', 'Dhaka', 2, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (33, 'Anika', 'Dhaka', 56, 'Engineer', 'Female', 50000);
INSERT INTO test_case_2.person VALUES (34, 'Ikra', 'Ctg', 78, 'Teacher', 'Female', 50000);
INSERT INTO test_case_2.person VALUES (35, 'Ojhor', 'Dhaka', 12, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (36, 'Saadman', 'Dhaka', 32, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (37, 'Nafiz', 'Dhaka', 15, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (38, 'Arman', 'Dhaka', 55, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (39, 'Faysal', 'Dhaka', 23, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (40, 'Syed', 'Dhaka', 22, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (41, 'Abidure', 'Dhaka', 21, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (42, 'Nafisa', 'Dhaka', 24, 'Engineer', 'Female', 50000);
INSERT INTO test_case_2.person VALUES (44, 'Abu', 'Ctg', 25, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (45, 'Maruf', 'Dhaka', 26, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (46, 'Omar', 'Dhaka', 27, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (47, 'Mahdia', 'Dhaka', 28, 'Engineer', 'Female', 50000);
INSERT INTO test_case_2.person VALUES (48, 'Nazneen', 'Dhaka', 29, 'Engineer', 'Female', 50000);
INSERT INTO test_case_2.person VALUES (49, 'Ahikul', 'Dhaka', 30, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (50, 'Asif', 'Dhaka', 31, 'Musician', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (51, 'Abir', 'Ctg', 32, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (52, 'Afrin', 'Dhaka', 22, 'Engineer', 'Female', 50000);
INSERT INTO test_case_2.person VALUES (53, 'Evan', 'Dhaka', 78, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (55, 'Muhib', 'Ctg', 66, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (56, 'Zizan', 'Dhaka', 90, 'Musician', 'Male', 40000);
INSERT INTO test_case_2.person VALUES (57, 'Tansi', 'Dhaka', 44, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (58, 'Mumu', 'Ctg', 87, 'Engineer', 'Female', 1000);
INSERT INTO test_case_2.person VALUES (59, 'Elma', 'Dhaka', 25, 'Teacher', 'Female',  9000);
INSERT INTO test_case_2.person VALUES (60, 'Emon', 'Dhaka', 33, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (61, 'Tanzil', 'Dhaka', 89, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (62, 'Nafi', 'Dhaka', 75, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (63, 'Azraf', 'Ctg', 54, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (64, 'Istiaque', 'Dhaka', 44, 'Engineer', 'Male', 1000);
INSERT INTO test_case_2.person VALUES (65, 'Ashraf', 'Dhaka', 32, 'Engineer', 'Male', 100);
INSERT INTO test_case_2.person VALUES (66, 'Rubaiat', 'Dhaka', 45, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (67, 'Rafsan', 'Dhaka', 2, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (68, 'Preetu', 'Dhaka', 12, 'Engineer', 'Female', 50000);
INSERT INTO test_case_2.person VALUES (69, 'Abdullah', 'Dhaka', 34, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (70, 'Shafi', 'Dhaka', 65, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (71, 'Nova', 'Ctg', 25, 'Engineer', 'Female', 200);
INSERT INTO test_case_2.person VALUES (72, 'Rokoni', 'Dhaka', 61, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (73, 'Alsaad', 'Dhaka', 40, 'Teacher', 'Male', 10000);
INSERT INTO test_case_2.person VALUES (74, 'Muhtasim', 'Dhaka', 39, 'Engineer', 'Male',3000);
INSERT INTO test_case_2.person VALUES (75, 'Galib', 'Jashore', 34, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (76, 'Keya', 'Dhaka', 45, 'Engineer', 'Female', 50000);
INSERT INTO test_case_2.person VALUES (77, 'Aunkon', 'Dhaka', 65, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (78, 'Sabbir', 'Dhaka', 53, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (80, 'Shams Shuvo', 'Dhaka', 21, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (81, 'Priota', 'Dhaka', 16, 'Engineer', 'Female', 50000);
INSERT INTO test_case_2.person VALUES (82, 'Tameem', 'Comilla', 18, 'Engineer', 'Male', 50000);
INSERT INTO test_case_2.person VALUES (83, 'Ibrahim', 'Dhaka', 19, 'Engineer', 'Male', 10);

INSERT INTO test_case_2.Phone VALUES (1, 'Samsung', 'galaxy note 8', 4);
INSERT INTO test_case_2.Phone VALUES (71, 'Xiaomi', 'Mi5', 6.5);
INSERT INTO test_case_2.Phone VALUES (58, 'Apple', 'Iphone 8', 7.0);
INSERT INTO test_case_2.Phone VALUES (51, 'Oneplus', 'three', 3);
INSERT INTO test_case_2.Phone VALUES (44, 'Blackberry', 'X50', 6.0);
INSERT INTO test_case_2.Phone VALUES (13, 'Samsung', 'galaxy s8', 7);
INSERT INTO test_case_2.Phone VALUES (28, 'Huwaei', 'Honor 5', 6.1);