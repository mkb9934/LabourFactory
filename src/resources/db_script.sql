CREATE TABLE mithlesh.labours(
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    wage INT,
    role VARCHAR(50),
    email VARCHAR(100)
);

CREATE TABLE attendance(
    id INT AUTO_INCREMENT PRIMARY KEY,
    labour_id INT NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NULL,
    FOREIGN KEY (labour_id) REFERENCES mithlesh.labours(id)
);

CREATE TABLE skills(
    id INT AUTO_INCREMENT PRIMARY KEY,
    labour_id INT NOT NULL,
    skill_name VARCHAR(100) NOT NULL,
    FOREIGN KEY (labour_id) REFERENCES mithlesh.labours(id)
);