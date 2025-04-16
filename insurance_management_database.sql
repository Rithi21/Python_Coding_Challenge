CREATE DATABASE insurance_management_db
USE insurance_management_db

create table user_info (
    user_id INT PRIMARY KEY,username VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL,role VARCHAR(30) NOT NULL)

create table policy (
    policy_id INT PRIMARY KEY,policy_name VARCHAR(75),
    policy_type VARCHAR(50),policy_amount DECIMAL(15, 2))

create table client (
    client_id INT PRIMARY KEY,client_name VARCHAR(100),
    contact_info VARCHAR(100),policy_id INT,
    FOREIGN KEY (policy_id) REFERENCES policy(policy_id))


create table claim (
    claim_id INT PRIMARY KEY,claim_number VARCHAR(50),date_filed DATE,claim_amount DECIMAL(15, 2),
    status VARCHAR(50),policy_id INT,client_id INT,
    FOREIGN KEY (policy_id) REFERENCES policy(policy_id),
    FOREIGN KEY (client_id) REFERENCES client(client_id))

create table payment (
    payment_id INT PRIMARY KEY,payment_date DATE,payment_amount DECIMAL(15, 2),client_id INT,
    FOREIGN KEY (client_id) REFERENCES client(client_id))

INSERT INTO user_info VALUES 
(1, 'Kamal', 'kamal123', 'admin'),
(2, 'Lakshmi', 'Luck345', 'agent')

INSERT INTO client VALUES 
(201, 'Priya John', 'priya12@gmail.com', 101),
(202, 'Rahul', 'rahul45@gmail.com', 102)

INSERT INTO claim VALUES 
(301, 'IN1001', '2024-03-15', 12000.00, 'Approved', 101, 201),
(302, 'IN1002', '2025-03-26', 25000.00, 'Pending', 102, 202)

INSERT INTO payment VALUES 
(401, '2024-04-01', 5000.00, 201),
(402, '2025-02-03', 7000.00, 202)

select * from policy
select * from client