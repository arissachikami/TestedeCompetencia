USE teste;

CREATE TABLE customers
(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    street VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(2) NOT NULL,
    credit_limit NUMERIC,
    PRIMARY KEY (id)
);

CREATE TABLE orders
(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    orders_date DATE,
	id_customers INT UNSIGNED DEFAULT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_orders_customers FOREIGN KEY(id_customers) REFERENCES customers(id)
);

INSERT INTO customers(nome,street,city,state,credit_limit)
VALUES
	('Nicolas Diogo Cardoso','Acesso um','Porto Alegre','RS','475'),
    ('Cecilia Olicustomersvia','Rua Sizuka','Cianorte','PR','3170'),
    ('Augusto Fernando','Rua Baldomiro','Palhoça','SC','1074'),
    ('Nicolas Cardoso','Acesso um','Porto Alegre','RS','475'),
    ('Sabrina Heloisa','Rua engenheiro Tito','Porto Alegre','RS','4312'),
    ('Joaquim Diego','Rua Vitoriano','Novo Hamburgo','RS','2345') ;
    
INSERT INTO orders(orders_date,id_customers)
VALUES 
	('2016-05-13','3'),
    ('2016-01-12','2'),
    ('2016-04-18','5'),
    ('2016-09-07','4'),
    ('2016-02-13','6'),
    ('2016-08-05','3');
    
SELECT customers.nome, orders.id FROM customers
INNER JOIN orders ON customers.id = orders.id_customers 
WHERE MONTH (orders.orders_date)<= 6 AND YEAR(orders.orders_date)= 2016 
ORDER BY orders.id ASC;