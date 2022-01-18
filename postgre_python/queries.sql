-- UPDATE employees
-- SET salary    = salary * 1.5,
--     job_title = 'sr. ' || job_title
-- WHERE job_title = 'System administrator'
--     AND ...
--
-- WHERE 1 = 1
--
-- -- 1000, 1200, 1300, 900, 2000
-- -- 1100, 1200, 1430, 900, 2000
-- -- 1210, 1200, 1573, 900, 2000

--
-- DELETE FROM countries
-- WHERE id = 3


--- Germany, Bulgaria
--- Munich , Burgas
---        , Sofia
---        , Plovdiv


-- SELECTION
SELECT *
FROM cities
WHERE country_id = 1;

-- Projection
SELECT name
FROM cities;

-- Projection + Selection
SELECT name
FROM cities
WHERE country_id = 1;


INSERT INTO countries(name, population)
VALUES ('Germany', 17),
       ('Poland', 11);

INSERT INTO cities(name, country_id)
VALUES ('Munich', 2),
       ('Warsaw', 3),
       ('Berlin', 2);

SELECT *
FROM cities;

SELECT cities.name as city, countries.name as country, countries.population
FROM cities
         JOIN countries
              ON cities.country_id = countries.id;


CREATE TABLE cities_full
AS
SELECT cities.name as city, countries.name as country
FROM cities
         JOIN countries
              ON cities.country_id = countries.id;

INSERT INTO cities_full
SELECT cities.name as city, countries.name as country
FROM cities
         JOIN countries
              ON cities.country_id = countries.id;

SELECT t.name AS city, c.name AS country, c.population
FROM cities AS t
         JOIN countries c
              ON t.country_id = c.id;


SELECT *
FROM employees e
         JOIN employees m
              ON e.manager_id = m.id;

-- Doncho (sr. Back-end developer) | Elena (Manager)


SELECT CONCAT(e.name, ' (', e.job_title, ')') as employee,
       CONCAT(m.name, ' (', m.job_title, ')') as manager
FROM employees e -- left
         RIGHT JOIN employees m -- right
                    ON e.manager_id = m.id;


SELECT DISTINCT country_id
FROM cities
ORDER BY country_id;

SELECT *
FROM employees
-- WHERE salary BETWEEN 1200 AND 1350
WHERE salary >= 1200
  AND 1350 >= salary;
--- 1200 <= salary <= 1350


--- Always false
SELECT NULL = NULL;
-- Correct
SELECT NULL is NULL;
SELECT NULL is not NULL;

SELECT t.name as city, c.name as country, c.population
FROM cities t
         JOIN countries c
              on c.id = t.country_id
ORDER BY c.name DESC, t.name
-- py: sorted(lambda x: (x.country_name, x.city_name), cities)


SELECT *
FROM countries c
         JOIN cities t
              ON c.id = t.country_id
         LEFT JOIN companies c2
                   ON t.id = c2.city_id;


SELECT *
FROM employees
WHERE manager_id is not NULL;


SELECT *
FROM countries c
         JOIN cities t
              ON c.id = t.country_id
         LEFT JOIN companies c2
                   ON t.id = c2.city_id;



SELECT CONCAT(e.name, ' (', e.job_title, ')') as employee,
       CONCAT(m.name, ' (', m.job_title, ')') as manager
FROM employees e -- left
         RIGHT JOIN employees m -- right
                    ON e.manager_id = m.id;

SELECT *
FROM cities_full;


SELECT *
FROM employees_managers;


SELECT c.name, count(country_id)
FROM cities t
         JOIN countries c
              ON t.country_id = c.id
GROUP BY country_id, c.name;
-- { '1': 4, '2': 2, '3': 1 }