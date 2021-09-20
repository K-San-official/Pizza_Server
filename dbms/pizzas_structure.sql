-- Create Database
CREATE DATABASE pizzas;
USE pizzas;

-- Create pizzza table
create table Pizza (
    pizza_id int NOT NULL AUTO_INCREMENT,
    pizza_name varchar(255) NOT NULL,
    pizza_price_euros int NOT NULL,
    pizza_price_cents int NOT NULL, PRIMARY KEY (pizza_id));


