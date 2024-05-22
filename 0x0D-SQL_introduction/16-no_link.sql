-- Lists all records of the table second_table.
FROM 'second_table'
SELECT 'score', 'name'
WHERE 'name' != ""
ORDER BY 'score' DESC;
