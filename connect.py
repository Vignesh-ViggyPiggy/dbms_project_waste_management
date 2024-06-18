import mysql.connector

def database_connect():
    database = mysql.connector.connect(
        host = "127.0.0.1",
        user = "project",
        password = "dawg",
        database = "project_database"
    
    )
    return database
#database = database_connect()
#if database.is_connected():
    #print("connected successfully")