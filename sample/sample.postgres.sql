CREATE DATABASE sample_db CHARACTER SET utf8;
GRANT ALL PRIVILEGES ON `sample_db`.* TO 'sample_user'@'%' IDENTIFIED BY 'sample_user';

CONNECT `sample_db`;

-- copyright: sakila-db

--
-- Table structure for table `category`
--

CREATE SEQUENCE category_seq;

CREATE TABLE category (
  category_id SMALLINT CHECK (category_id > 0) NOT NULL DEFAULT NEXTVAL ('category_seq'),
  name VARCHAR(25) NOT NULL,
  last_update TIMESTAMP(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY  (category_id)
);


--
-- Dumping data for table category
--

AUTOCOMMIT:=0;
INSERT INTO category VALUES (1,'Action','2006-02-15 04:46:27'),
(2,'Animation','2006-02-15 04:46:27'),
(3,'Children','2006-02-15 04:46:27'),
(4,'Classics','2006-02-15 04:46:27'),
(5,'Comedy','2006-02-15 04:46:27'),
(6,'Documentary','2006-02-15 04:46:27'),
(7,'Drama','2006-02-15 04:46:27'),
(8,'Family','2006-02-15 04:46:27'),
(9,'Foreign','2006-02-15 04:46:27'),
(10,'Games','2006-02-15 04:46:27'),
(11,'Horror','2006-02-15 04:46:27'),
(12,'Music','2006-02-15 04:46:27'),
(13,'New','2006-02-15 04:46:27'),
(14,'Sci-Fi','2006-02-15 04:46:27'),
(15,'Sports','2006-02-15 04:46:27'),
(16,'Travel','2006-02-15 04:46:27');
COMMIT;

-- vim: ft=sql :
