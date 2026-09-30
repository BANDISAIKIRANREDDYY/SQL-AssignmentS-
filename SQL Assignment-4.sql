USE sakila;

-- 1. List all customers along with the films they have rented.
SELECT c.customer_id,
       c.first_name,
       c.last_name,
       f.title
FROM customer AS c
LEFT JOIN rental AS r ON r.customer_id = c.customer_id
LEFT JOIN inventory AS i ON i.inventory_id = r.inventory_id
LEFT JOIN film AS f ON f.film_id = i.film_id
ORDER BY c.customer_id, f.title;


-- 2. List all customers and show their rental count, including those who haven't rented any films.
SELECT c.customer_id,
       c.first_name,
       c.last_name,
       COUNT(r.rental_id) AS rental_count
FROM customer AS c
LEFT JOIN rental AS r ON r.customer_id = c.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY rental_count DESC;


-- 3.  Show all films along with their category. Include films that don't have a category assigned.
SELECT f.film_id,
       f.title,
       c.name AS category
FROM film AS f
LEFT JOIN film_category AS fc ON fc.film_id = f.film_id
LEFT JOIN category AS c ON c.category_id = fc.category_id
ORDER BY f.title;


-- 4. Show all customers and staff emails from both customer and staff tables using a full outer join (simulate using LEFT + RIGHT + UNION).

SELECT c.customer_id,
       c.email AS customer_email,
       s.staff_id,
       s.email AS staff_email
FROM customer AS c
LEFT JOIN staff AS s ON s.email = c.email

UNION

SELECT c.customer_id,
       c.email AS customer_email,
       s.staff_id,
       s.email AS staff_email
FROM customer AS c
RIGHT JOIN staff AS s ON s.email = c.email;


-- 5. Find all actors who acted in the film "ACADEMY DINOSAUR".
SELECT a.actor_id,
       a.first_name,
       a.last_name
FROM actor AS a
JOIN film_actor AS fa ON fa.actor_id = a.actor_id
JOIN film AS f ON f.film_id = fa.film_id
WHERE f.title = 'ACADEMY DINOSAUR'
ORDER BY a.last_name, a.first_name;


-- 6.List all stores and the total number of staff members working in each store, even if a store has no staff.
SELECT s.store_id,
       COUNT(st.staff_id) AS staff_count
FROM store AS s
LEFT JOIN staff AS st ON st.store_id = s.store_id
GROUP BY s.store_id
ORDER BY s.store_id;


-- 7. List the customers who have rented films more than 5 times. Include their name and total rental count.
SELECT c.customer_id,
       c.first_name,
       c.last_name,
       COUNT(r.rental_id) AS total_rentals
FROM customer AS c
JOIN rental AS r ON r.customer_id = c.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
HAVING COUNT(r.rental_id) > 5
ORDER BY total_rentals DESC;