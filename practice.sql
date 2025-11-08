-- practice
CREATE DATABASE company_db;

USE company_db;

CREATE TABLE employees (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  department VARCHAR(50),
  salary DECIMAL(10,2)
);

INSERT INTO employees (name, department, salary) 
VALUES ('Satish', 'QA', 55000.00), ('Priya', 'Dev', 60000.00), ('Amit', 'HR', 45000.00);

SELECT department, AVG(salary) AS average_salary 
FROM employees 
GROUP BY department;



-- practice2
USE company_db;

CREATE TABLE departments (
  dept_id INT AUTO_INCREMENT PRIMARY KEY,
  dept_name VARCHAR(50)
);

INSERT INTO departments (dept_name) 
VALUES ('QA'), ('Development'), ('HR');

SELECT e.name, e.department, d.dept_name
FROM employees e
JOIN departments d
ON e.department = d.dept_name;

UPDATE employees 
SET salary = salary 5000 
WHERE department = 'QA';




