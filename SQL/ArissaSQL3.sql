USE schema3;

CREATE TABLE categories(
	id int unsigned not null auto_increment,
    nome varchar(50) not null,
    PRIMARY KEY(id)
);
CREATE TABLE products(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome_products VARCHAR(50) NOT NULL,
    amount NUMERIC,
    price DECIMAL(10,2),
    id_categories INT UNSIGNED DEFAULT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_products_categories FOREIGN KEY (id_categories) REFERENCES categories(id)
);

INSERT INTO categories(nome)
VALUES 
	 ('wood'),
	 ('Luxery'),
	 ('Vintage'),
	 ('Mordern'),
	 ('Super Luxery');
	
INSERT INTO products(nome_products, amount, price,id_categories)
VALUES
 ('Two-doors warddrobe','100','800.00','1'),
 ('Dining table','1000','500.00','3'),
 ('Tower holder','10000','25.50','4'),
 ('Computer desk','350','320.50','2'),
 ('Chair','3000','210.64','4'),
 ('Single bed','750','460.00','1');
 
SELECT categories.nome AS category_name, 
       SUM(products.amount) AS total_amount
FROM products
INNER JOIN categories ON products.id_categories = categories.id
GROUP BY categories.nome;