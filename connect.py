import mysql.connector

database = mysql.connector.connect(
    host = "127.0.0.1",
    user = "project",
    password = "dawg",
    database = "project_database"
)
if database.is_connected():
    print("connected successfully")