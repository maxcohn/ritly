CREATE SCHEMA IF NOT EXISTS `linkstore`;

USE linkstore;
CREATE TABLE IF NOT EXISTS Links (
	Url varchar(10),
    Link varchar(255)
);
