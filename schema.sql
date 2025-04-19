-- Create the database
CREATE DATABASE IF NOT EXISTS employees;
USE employees;

-- Table for login credentials
CREATE TABLE IF NOT EXISTS log_id (
    user_id VARCHAR(50) NOT NULL PRIMARY KEY,
    password VARCHAR(10) NOT NULL
);

-- Sample login entries
INSERT INTO log_id (user_id, password) VALUES
('hari', '6054'),
('admin', '1234');

-- Table for employee details
CREATE TABLE IF NOT EXISTS office (
    v_em_no INT PRIMARY KEY,
    v_em_name VARCHAR(50),
    v_em_dept VARCHAR(50),
    v_em_salary INT,
    v_em_age INT
);

-- Sample employee entries
INSERT INTO office (v_em_no, v_em_name, v_em_dept, v_em_salary, v_em_age) VALUES
(101, 'Ajay', 'HR', 40000, 30),
(102, 'Vijay', 'IT', 60000, 28),
(103, 'Arun', 'Marketing', 45000, 35);

-- Table for employee performance
CREATE TABLE IF NOT EXISTS v_em_performance (
    v_em_no INT,
    v_em_name VARCHAR(50),
    v_em_dept VARCHAR(50),
    v_em_performance TEXT,
    v_em_work INT,
    FOREIGN KEY (v_em_no) REFERENCES office(v_em_no)
);

-- Sample performance entries
INSERT INTO v_em_performance (v_em_no, v_em_name, v_em_dept, v_em_performance, v_em_work) VALUES
(101, 'Ajay', 'HR', 'Excellent', 5),
(102, 'Vijay', 'IT', 'Good', 3),
(103, 'Arun', 'Marketing', 'Average', 7);
