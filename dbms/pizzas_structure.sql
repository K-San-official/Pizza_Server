-- Create Database
CREATE DATABASE pizzas;
USE pizzas;

-- Create pizzza table
CREATE TABLE pizza(
        id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
        name varchar(255),
        price decimal(16,2)
)
