# SQL exercice

## Project description
Here is an exercice showing my SQL knowledge.

### Retrieve after hours failed login attempts
`SELECT * FROM log_in_attempts WHERE login_time > '18:00:00' AND legin_success = FALSE;`

### Retrieve login attempts on specific dates
`SELECT * FROM log_in_attempts WHERE login_date = '2026-06-16';`

### Retrieve login attempts outside of Mexico
`SELECT * FROM log_in_attempts WHERE NOT country = 'Mexico';`

### Retrieve employees in Marketing
`SELECT * FROM employees WHERE department = 'Marketing';`

### Retrieve employees in East building
`SELECT * FROM employees WHERE office LIKE 'East%';`

### Retrieve employees in Finance or Sales
`SELECT * FROM employees WHERE department = 'Finance' OR department = 'Sales'`

### Retrieve all employees not in IT
`SELECT * FROM employees WHERE NOT department = 'IT'`

### Retrieve all rows matching on a specific column existing in 2 tables
`SELECT * FROM employees INNER JOIN machines ON employees.employee_id = machines.employee_id;`

### Retrieve all rows from one table and matching lines in another table
`SELECT * FROM log_in_attemps LEFT JOIN employees ON log_in_attemps.employee_id = employees.employee_id`

## Summary
`SELECT * FROM`, `ORDER BY`, `WHERE`, `> < >= <= != =`, `WHERE NOT`, `BETWEEN AND`, `AND`, `OR`, `INNER JOIN`, `LEFT/RIGHT JOIN`, `FULL OUTER JOIN`