CREATE DATABASE music WITH OWNER = postgres;

\c music

CREATE TABLE IF NOT EXISTS artist (
    id int,
    rating int
);

INSERT INTO artist VALUES (0,4);
INSERT INTO artist VALUES (1,10);