CREATE TABLE accounts(
    id INTEGER,
    username varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    phone varchar(255) NOT NULL
);

INSERT INTO accounts (id, username, password, phone) VALUES
    (1, "user1", "password1", "10.64.13.1");