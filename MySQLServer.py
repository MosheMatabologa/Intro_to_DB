import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server
        conn = mysql.connector.connect(
            host="localhost",  # Change this if your MySQL server is remote
            user="root",  # Change this to your MySQL username
            password="yourpassword"  # Change this to your MySQL password
        )

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error:
        print("mysql.connector.Error")
        
    #except Error as e:
        print(f"["except mysql.connector.Error": {e}")
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
