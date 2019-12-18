-- Database: hunquery

-- DROP DATABASE hunquery;

CREATE DATABASE hunquery
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- CREATE TABLE
-- DROP TABLE IF EXISTS recipes;

CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    recipe_name VARCHAR(70) NOT NULL,
    cuisine VARCHAR(50) NOT NULL,
    "type" VARCHAR(50) NOT NULL,
    calories INT,
    url VARCHAR(100) NOT NULL,
);
SELECT * FROM recipes;
