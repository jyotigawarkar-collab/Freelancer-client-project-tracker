import mysql.connector

try:
    connection = mysql.connector.connect(
        host="YOUR_HOST",
        port=YOUR_PORT,
        user="YOUR_USER",
        password="YOUR_PASSWORD",
        database="YOUR_DATABASE",
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