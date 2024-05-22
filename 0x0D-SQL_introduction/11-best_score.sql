-- Lists all records with a score >= 10 in the table second_table.
FROM 'second_table'
SELECT 'score', 'name'
WHERE 'score' >= 10
ORDER BY 'score' DESC;

