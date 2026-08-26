CREATE TABLE websites (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    url VARCHAR(255) NOT NULL,
    status VARCHAR(20) DEFAULT 'UNKNOWN'
);

INSERT INTO websites (name, url, status)
VALUES
    ('Google', 'https://google.com', 'UP'),
    ('GitHub', 'https://github.com', 'UP');
