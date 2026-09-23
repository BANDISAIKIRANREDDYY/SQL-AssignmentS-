USE sakila;

-- 1. Identify if there are duplicates in Customer table. Don't use customer id to check the duplicates
SELECT first_name, last_name,email,
COUNT(*) AS duplicate_count FROM customer
GROUP BY first_name, last_name, email
HAVING COUNT(*) > 1;


-- 2. Number of times letter 'a' is repeated in film descriptions
SELECT film_id, title,
       CHAR_LENGTH(COALESCE(description, ''))
       - CHAR_LENGTH(
           REPLACE(LOWER(COALESCE(description, '')), 'a', '')
         ) AS a_count FROM film;


-- 3. Number of times each vowel is repeated in film descriptions 
SELECT film_id,
       title,
       CHAR_LENGTH(text_description)
         - CHAR_LENGTH(REPLACE(text_description, 'a', '')) AS a_count,
       CHAR_LENGTH(text_description)
         - CHAR_LENGTH(REPLACE(text_description, 'e', '')) AS e_count,
       CHAR_LENGTH(text_description)
         - CHAR_LENGTH(REPLACE(text_description, 'i', '')) AS i_count,
       CHAR_LENGTH(text_description)
         - CHAR_LENGTH(REPLACE(text_description, 'o', '')) AS o_count,
       CHAR_LENGTH(text_description)
         - CHAR_LENGTH(REPLACE(text_description, 'u', '')) AS u_count
FROM (SELECT film_id, title,
        LOWER(COALESCE(description, '')) AS text_description FROM film) AS film_descriptions;


-- 4.1. Display the payments made by each customer, month wise
SELECT c.customer_id,
       c.first_name,
       c.last_name,
       DATE_FORMAT(p.payment_date, '%Y-%m') AS payment_month,
       SUM(p.amount) AS total_paid
FROM customer AS c
JOIN payment AS p ON p.customer_id = c.customer_id
GROUP BY c.customer_id,
         c.first_name,
         c.last_name,
         DATE_FORMAT(p.payment_date, '%Y-%m')
ORDER BY c.customer_id, payment_month;


-- 4.2. Display the payments made by each customer, year wise
SELECT c.customer_id,
       c.first_name,
       c.last_name,
       YEAR(p.payment_date) AS payment_year,
       SUM(p.amount) AS total_paid
FROM customer AS c
JOIN payment AS p ON p.customer_id = c.customer_id
GROUP BY c.customer_id,
         c.first_name,
         c.last_name,
         YEAR(p.payment_date)
ORDER BY c.customer_id, payment_year;


-- 4.3. Display the payments made by each customer, week wise
SELECT c.customer_id,
       c.first_name,
       c.last_name,
       DATE_FORMAT(p.payment_date, '%x-W%v') AS payment_week,
       SUM(p.amount) AS total_paid
FROM customer AS c
JOIN payment AS p ON p.customer_id = c.customer_id
GROUP BY c.customer_id,
         c.first_name,
         c.last_name,
         DATE_FORMAT(p.payment_date, '%x-W%v')
ORDER BY c.customer_id, payment_week;


-- 5.Check if any given year is a leap year or not. You need not consider any table from sakila database. Write within the select query with hardcoded date
SELECT YEAR('2024-01-01') AS given_year, CASE
           WHEN DAY(LAST_DAY('2024-02-01')) = 29
               THEN 'Leap year'
           ELSE 'Not a leap year'
       END AS leap_year_status;


-- 6. Display number of days remaining in the current year from today.
SELECT CURDATE() AS today,
DATEDIFF(MAKEDATE(YEAR(CURDATE()) + 1, 1),
CURDATE() ) - 1 AS days_remaining;


-- 7. Display quarter number(Q1,Q2,Q3,Q4) for the payment dates from payment table.
SELECT payment_id,
       customer_id,
       payment_date,
       CONCAT('Q', QUARTER(payment_date)) AS payment_quarter
FROM payment
ORDER BY payment_date, payment_id;





