USE sakila;

-- SUBQUERIES: Questions 1–3

-- 1.Display all customer details who have made more than 5 payments.
SELECT * FROM customer
WHERE customer_id IN (
    SELECT customer_id
    FROM payment
    GROUP BY customer_id
    HAVING COUNT(*) > 5 );


-- 2.Find the names of actors who have acted in more than 10 films.
SELECT actor_id, first_name, last_name FROM actor
WHERE actor_id IN (
    SELECT actor_id
    FROM film_actor
    GROUP BY actor_id
    HAVING COUNT(*) > 10 );


-- 3.  Find the names of customers who never made a payment.
SELECT COUNT(*) AS customers_without_payments
FROM sakila.customer AS c
WHERE NOT EXISTS (SELECT 1
    FROM sakila.payment AS p
    WHERE p.customer_id = c.customer_id);


-- CTEs: Questions 4–6

-- 4. List all films whose rental rate is higher than the average rental rate of all films.
WITH average_rate AS (SELECT AVG(rental_rate) AS avg_rental_rate FROM film)
SELECT f.film_id, f.title, f.rental_rate
FROM film AS f
CROSS JOIN average_rate AS a
WHERE f.rental_rate > a.avg_rental_rate;

-- 5.List the titles of films that were never rented.
WITH rented_films AS (SELECT DISTINCT i.film_id FROM inventory AS i
JOIN rental AS r ON r.inventory_id = i.inventory_id)
SELECT f.film_id, f.title FROM film AS f
LEFT JOIN rented_films AS rf ON rf.film_id = f.film_id
WHERE rf.film_id IS NULL;


-- 6. Display the customers who rented films in the same month as customer with ID 5.
WITH customer_5_months AS (SELECT DISTINCT EXTRACT(YEAR_MONTH FROM rental_date) AS rental_month
FROM rental WHERE customer_id = 5)
SELECT DISTINCT c.customer_id, c.first_name, c.last_name
FROM customer AS c
JOIN rental AS r ON r.customer_id = c.customer_id
JOIN customer_5_months AS m
    ON EXTRACT(YEAR_MONTH FROM r.rental_date) = m.rental_month
WHERE c.customer_id <> 5;


-- VIEWS: Questions 7–9

-- 7. Find all staff members who handled a payment greater than the average payment amount.
CREATE OR REPLACE VIEW assignment_staff_above_avg_payment AS
SELECT s.staff_id, s.first_name, s.last_name
FROM staff AS s
WHERE EXISTS (SELECT 1
    FROM payment AS p
    WHERE p.staff_id = s.staff_id
      AND p.amount > (SELECT AVG(amount) FROM payment));

SELECT * FROM assignment_staff_above_avg_payment;


-- 8. Show the title and rental duration of films whose rental duration is greater than the average.
CREATE OR REPLACE VIEW assignment_long_rental_duration AS
SELECT title, rental_duration
FROM film
WHERE rental_duration > (SELECT AVG(rental_duration) FROM film);
SELECT * FROM assignment_long_rental_duration;


-- 9. Find all customers who have the same address as customer with ID 1.
CREATE OR REPLACE VIEW sakila.assignment_same_address AS
SELECT c.*
FROM sakila.customer AS c
JOIN sakila.customer AS reference_customer
    ON c.address_id = reference_customer.address_id
WHERE reference_customer.customer_id = 1;

-- TEMPORARY TABLE: Question 10


-- 10. List all payments that are greater than the average of all payments.

DROP TEMPORARY TABLE IF EXISTS temp_above_average_payments;

CREATE TEMPORARY TABLE temp_above_average_payments AS
SELECT * FROM payment
WHERE amount > (SELECT AVG(amount) FROM payment);
SELECT * FROM temp_above_average_payments ORDER BY amount DESC;





