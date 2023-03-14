USE videojuegosmodels;
/*CREATE TABLE videojuegos(ID INT(50) NOT NULL,title VARCHAR(30) NOT NULL,genre VARCHAR(60) NOT NULL,release_year INT NOT NULL,PRIMARY KEY(ID));*/

/*INSERT INTO videojuegos VALUE (2, "Dead Cells", "Metroidvania", 2018);

SELECT * FROM videojuegos;

/*SELECT @@datadir;*/

DROP TABLE videojuegos;
CREATE TABLE publishers(ID INT NOT NULL,publisher VARCHAR(30) NOT NULL,country VARCHAR(60) NOT NULL,foundation_year INT NOT NULL,founder VARCHAR(30),PRIMARY KEY(ID));
CREATE TABLE developers(ID INT NOT NULL,developer VARCHAR(30) NOT NULL,country VARCHAR(60) NOT NULL,foundation_year INT NOT NULL,PRIMARY KEY(ID));

SELECT * FROM videojuegos;

CREATE TABLE videojuegos(ID INT NOT NULL,title VARCHAR(30) NOT NULL,genre VARCHAR(60) NOT NULL,release_year INT NOT NULL,developer VARCHAR(30), publisher VARCHAR(30),PRIMARY KEY(ID));

INSERT INTO videojuegos VALUE (1, "Dead Cells", "Metroidvania", 2018, "MotionTwin", "Playdigious");

INSERT INTO developers VALUE (1, "MotionTwin", "France", 2001);

INSERT INTO publishers VALUE (1, "Playdigious", "France", 2015, "Xavier Liard");

SELECT * FROM videojuegos;
SELECT * FROM developers;
SELECT * FROM publishers;

ALTER TABLE videojuegos ADD FOREIGN KEY (developer) REFERENCES developers(developer);

ALTER TABLE videojuegos ADD FOREIGN KEY (publisher) REFERENCES publishers(publisher);

ALTER TABLE developers ADD FOREIGN KEY (developer) REFERENCES videojuegos(developer);