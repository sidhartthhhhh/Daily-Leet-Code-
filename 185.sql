# Write your MySQL query statement below
WITH RankedEmployees AS (
    -- Step 1: Rank employees within each department based on salary
    SELECT
        name,
        salary,
        departmentId,
        DENSE_RANK() OVER (
            PARTITION BY departmentId 
            ORDER BY salary DESC
        ) AS salary_rank
    FROM
        Employee
)
-- Step 2: Join with Department table and filter for top 3 ranks
SELECT
    d.name AS Department,
    re.name AS Employee,
    re.salary AS Salary
FROM
    RankedEmployees re
JOIN
    Department d ON re.departmentId = d.id
WHERE
    re.salary_rank <= 3;ac