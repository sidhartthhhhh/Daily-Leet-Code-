/*
 This query uses a recursive CTE to iterate through the string, 
 part by part, where a "part" is separated by a space or a hyphen.
*/
WITH RECURSIVE Processed AS (
    -- Base case: Start with the original text, empty converted text
    SELECT
        content_id,
        content_text AS original_text,
        -- Use CAST AS CHAR(1000) for MySQL compatibility
        CAST('' AS CHAR(1000)) AS converted_text,
        CAST(content_text AS CHAR(1000)) AS remaining_text
    FROM
        user_content
    
    UNION ALL
    
    -- Recursive step: Process one "part" at a time
    SELECT
        content_id,
        original_text,
        
        -- 1. BUILD THE 'converted_text'
        CAST(
            CONCAT(
                converted_text,
                -- Capitalize the first letter of the current part
                UPPER(LEFT(remaining_text, 1)),
                
                -- Lowercase the rest of the current part
                LOWER(
                    SUBSTRING(remaining_text, 2, 
                        -- Find the length of the rest of the part
                        CASE 
                            -- Find the position of the next delimiter (' ' or '-')
                            WHEN LEAST(
                                -- Use 99999 as a large number for "not found"
                                CASE WHEN LOCATE(' ', remaining_text) = 0 THEN 99999 ELSE LOCATE(' ', remaining_text) END,
                                CASE WHEN LOCATE('-', remaining_text) = 0 THEN 99999 ELSE LOCATE('-', remaining_text) END
                            ) = 99999
                            THEN LENGTH(remaining_text) -- It's the last part
                            ELSE LEAST(
                                CASE WHEN LOCATE(' ', remaining_text) = 0 THEN 99999 ELSE LOCATE(' ', remaining_text) END,
                                CASE WHEN LOCATE('-', remaining_text) = 0 THEN 99999 ELSE LOCATE('-', remaining_text) END
                            ) - 1 -- Length up to (but not including) the delimiter
                        END - 1 -- -1 because SUBSTRING starts at char 2
                    )
                ),
                
                -- Append the delimiter itself (if one was found)
                CASE 
                    WHEN LEAST(
                        CASE WHEN LOCATE(' ', remaining_text) = 0 THEN 99999 ELSE LOCATE(' ', remaining_text) END,
                        CASE WHEN LOCATE('-', remaining_text) = 0 THEN 99999 ELSE LOCATE('-', remaining_text) END
                    ) = 99999
                    THEN '' -- No delimiter, it was the last part
                    ELSE SUBSTRING(remaining_text, 
                        LEAST(
                            CASE WHEN LOCATE(' ', remaining_text) = 0 THEN 99999 ELSE LOCATE(' ', remaining_text) END,
                            CASE WHEN LOCATE('-', remaining_text) = 0 THEN 99999 ELSE LOCATE('-', remaining_text) END
                        ), 1)
                END
            )
        AS CHAR(1000)) AS converted_text,
        
        -- 2. UPDATE THE 'remaining_text'
        CAST(
            CASE 
                WHEN LEAST(
                    CASE WHEN LOCATE(' ', remaining_text) = 0 THEN 99999 ELSE LOCATE(' ', remaining_text) END,
                    CASE WHEN LOCATE('-', remaining_text) = 0 THEN 99999 ELSE LOCATE('-', remaining_text) END
                ) = 99999
                THEN '' -- No text left, processing is done
                ELSE SUBSTRING(remaining_text, 
                    -- Start from the character AFTER the delimiter
                    LEAST(
                        CASE WHEN LOCATE(' ', remaining_text) = 0 THEN 99999 ELSE LOCATE(' ', remaining_text) END,
                        CASE WHEN LOCATE('-', remaining_text) = 0 THEN 99999 ELSE LOCATE('-', remaining_text) END
                    ) + 1
                )
            END
        AS CHAR(1000)) AS remaining_text
        
    FROM
        Processed
    WHERE
        -- Continue as long as there is text remaining
        LENGTH(remaining_text) > 0
)

-- Final result: Select the rows where processing is complete
SELECT
    content_id,
    original_text,
    converted_text
FROM
    Processed
WHERE
    -- The final, fully converted string is in the row
    -- where 'remaining_text' has become empty.
    LENGTH(remaining_text) = 0
-- Add ORDER BY to ensure a stable output for the test case
ORDER BY
    content_id;
