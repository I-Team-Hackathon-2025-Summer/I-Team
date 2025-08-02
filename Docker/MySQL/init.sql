DROP DATABASE tabitalk;
DROP USER 'Iteam';

CREATE USER 'Iteam' IDENTIFIED BY 'Iteam';
CREATE DATABASE tabitalk;
USE tabitalk
GRANT ALL PRIVILEGES ON tabitalk.* TO 'Iteam';

CREATE TABLE users (
    user_id VARCHAR(255) PRIMARY KEY,
    user_name VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE open_channels (
    channel_id INT AUTO_INCREMENT PRIMARY KEY,
    area_id INT,
    prefecture VARCHAR(255) NOT NULL
);

CREATE TABLE areas (
    area_id INT AUTO_INCREMENT PRIMARY KEY,
    channel_id INT NOT NULL,
    area_name VARCHAR(255) UNIQUE NOT NULL
);


CREATE TABLE open_messages (
    message_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    message TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

INSERT INTO users(user_id, user_name, email, password) VALUES('970af84c-dd40-47ff-af23-282b72b7cca8','テスト','test@gmail.com','testtest123');