DROP TABLE IF EXISTS score;
CREATE TABLE score
(
    id      	serial  NOT NULL PRIMARY KEY,
    user_name  varchar(50) NOT NULL,
    score	float NOT NULL,
    difficulty  varchar(10) NOT NULL
);

