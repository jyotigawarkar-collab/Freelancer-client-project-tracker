import mysql.connector

try:
    connection = mysql.connector.connect(
        host="freelancertracker-prashuu374-3195.j.aivencloud.com",
        port=26001,
        user="avnadmin",
        password="AVNS_JfYahiWEsndTWjUJW19",
        database="defaultdb",
        ssl_disabled=False
    )

    cursor = connection.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        )
    """)

    # Clients table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            client_id INT AUTO_INCREMENT PRIMARY KEY,
            client_name VARCHAR(100) NOT NULL,
            email VARCHAR(100),
            phone VARCHAR(20),
            company VARCHAR(100),
            address VARCHAR(255)
        )
    """)

    # Projects table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            project_id INT AUTO_INCREMENT PRIMARY KEY,
            client_id INT NOT NULL,
            project_name VARCHAR(150) NOT NULL,
            category VARCHAR(100),
            start_date DATE,
            deadline DATE,
            budget DECIMAL(10,2) DEFAULT 0,
            amount_paid DECIMAL(10,2) DEFAULT 0,
            status VARCHAR(30) DEFAULT 'Pending',
            description TEXT,
            FOREIGN KEY (client_id)
                REFERENCES clients(client_id)
                ON DELETE CASCADE
        )
    """)

    connection.commit()

    print("✅ Database tables created successfully!")

    cursor.close()
    connection.close()

except Exception as e:
    print("❌ Error:", e)