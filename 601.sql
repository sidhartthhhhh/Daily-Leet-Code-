# Write your MySQL query statement below
WITH FilteredStadium AS (
    -- Filtering for records with 100 or more people
    SELECT
        id,
        visit_date,
        people
    FROM
        Stadium
    WHERE
        people >= 100
),
GroupedStadium AS (
    -- Identifing consecutive 'islands' (groups) of IDs
    -- I'm doing this by subtracting a row number from the id.
    SELECT
        id,
        visit_date,
        people,
        (id - ROW_NUMBER() OVER (ORDER BY id)) AS group_id
    FROM
        FilteredStadium
),
ValidGroups AS (
    -- Finding which groups have 3 or more consecutive records
    SELECT
        group_id
    FROM
        GroupedStadium
    GROUP BY
        group_id
    HAVING
        COUNT(*) >= 3
)
-- Step 4: Select all original records that belong to a valid group
SELECT
    gs.id,
    gs.visit_date,
    gs.people
FROM
    GroupedStadium gs
JOIN
    ValidGroups vg ON gs.group_id = vg.group_id
ORDER BY
    gs.visit_date;