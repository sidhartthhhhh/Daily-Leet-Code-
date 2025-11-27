# Write your MySQL query statement below
SELECT
    t.request_at AS Day,
    ROUND(
        -- Calculating  the average: 1.0 for cancelled, 0.0 for completed
        AVG(
            CASE 
                WHEN t.status = 'completed' THEN 0.0
                ELSE 1.0 
            END
        )
    , 2) AS "Cancellation Rate"
FROM
    Trips t
WHERE
    -- 1. Filtering by the required dates
    t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
    
    -- 2. to ensure the client is not banned
    AND t.client_id IN (
        SELECT users_id FROM Users WHERE banned = 'No'
    )
    
    -- 3. to ensure the driver is not banned
    AND t.driver_id IN (
        SELECT users_id FROM Users WHERE banned = 'No'
    )
GROUP BY
    t.request_at
ORDER BY
    Day;