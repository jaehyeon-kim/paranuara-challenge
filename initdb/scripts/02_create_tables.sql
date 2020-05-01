DROP TABLE IF EXISTS paranuara.employees;
DROP TABLE IF EXISTS paranuara.companies;
DROP TABLE IF EXISTS paranuara.favourite_food;
DROP TABLE IF EXISTS paranuara.friends;

CREATE TABLE paranuara.employees (
	id int NOT NULL,
	name varchar(30) NOT NULL,
    age int NOT NULL,
    address varchar(200) NOT NULL,
    phone varchar(30) NOT NULL,
    eye_colour varchar(10) NOT NULL,
    has_died  boolean NOT NULL,
    company_id int NOT NULL,
    CONSTRAINT persons_pk PRIMARY KEY (id)
);

CREATE TABLE paranuara.companies (
	id int NOT NULL,
	name varchar(30) NOT NULL,
    CONSTRAINT companies_pk PRIMARY KEY (id)
);

CREATE TABLE paranuara.favourite_food (
	id serial NOT NULL,
    employee_id int NOT NULL,
	name varchar(30) NOT NULL,
    CONSTRAINT favourite_food_pk PRIMARY KEY (id)
);

CREATE TABLE paranuara.friends (
	id serial NOT NULL,
    employee_id int NOT NULL,
	friend_id int NOT NULL,
    CONSTRAINT friends_pk PRIMARY KEY (id)
);