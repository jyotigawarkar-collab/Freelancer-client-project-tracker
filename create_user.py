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

    username = "ADMIN"
    password = "ADMIN@123"

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (username, password)
    )

    connection.commit()

    print("✅ Login user created successfully!")
    print("Username:", username)
    print("Password:", password)

    cursor.close()
    connection.close()

except Exception as e:
    print("❌ Error:", e)