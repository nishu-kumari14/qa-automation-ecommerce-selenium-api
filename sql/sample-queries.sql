-- Basic table read queries
SELECT * FROM users;
SELECT * FROM orders WHERE status = 'completed';

-- Find all pending orders for validation follow-up
SELECT order_id, user_id, status, created_at
FROM orders
WHERE status = 'pending';

-- Validate total completed orders by user
SELECT user_id, COUNT(*) AS completed_order_count
FROM orders
WHERE status = 'completed'
GROUP BY user_id
ORDER BY completed_order_count DESC;

-- Join users and orders to validate ownership and order states
SELECT u.user_id, u.name, o.order_id, o.status, o.total_amount
FROM users u
JOIN orders o ON u.user_id = o.user_id
ORDER BY o.created_at DESC;

-- Filter orders completed within a date range
SELECT order_id, user_id, total_amount, completed_at
FROM orders
WHERE status = 'completed'
  AND completed_at BETWEEN '2026-03-01' AND '2026-03-31';
