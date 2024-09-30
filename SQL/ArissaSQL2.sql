USE schema2;

CREATE TABLE categories(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
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
	 ('superios'),
	 ('Super Luxery'),
	 ('Mordern'),
	 ('Nerd'),
	 ('Infantile');
	
INSERT INTO products(nome_products, amount, price,id_categories)
VALUES
 ('Blue chair','30','300.00','9'),
 ('Red chair','200','2150.00','2'),
 ('Disney Wardrobe','400','829.50','4'),
 ('Blue Toaster','20','9.90','3'),
 ('Solar Panel','30','300.25','4');
 
UPDATE categories
SET nome = 'Super Luxury'
WHERE id = 2;

SELECT products.nome_products AS product_name, categories.nome AS category_name 
FROM products
INNER JOIN categories ON products.id_categories = categories.id 
WHERE products.amount>100 AND products.id_categories IN (1,2,3,6,9) 
ORDER BY categories.id ASC;
 
