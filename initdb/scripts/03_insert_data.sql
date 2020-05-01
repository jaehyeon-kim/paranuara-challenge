COPY paranuara.employees(id, name, age, address, phone, eye_colour, has_died, company_id)
FROM '/tmp/employees.csv' DELIMITER ',' CSV;

COPY paranuara.companies(id, name)
FROM '/tmp/companies.csv' DELIMITER ',' CSV;

COPY paranuara.favourite_food(employee_id, name)
FROM '/tmp/favourite_food.csv' DELIMITER ',' CSV;

COPY paranuara.friends(employee_id, friend_id)
FROM '/tmp/friends.csv' DELIMITER ',' CSV;
