--1873. Calculate Special Bonus
SELECT employee_id, 
    CAST (CASE WHEN employee_id%2 = 1 AND name NOT LIKE 'm%'
        THEN salary
        ELSE 0
        END AS int) AS bonus
FROM Employees
ORDER BY employee_id


-- 627. Swap Salary
UPDATE salary SET sex = CASE WHEN sex = 'm' THEN 'f' ELSE 'm' END    


-- 196. Delete Duplicate Emails
DELETE p1 FROM Person p1
INNER JOIN Person p2
ON p1.[email]=p2.[email] AND p1.[id]>p2.[id]