from django.db import connection

def create_table():
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sample_table (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255)
            );
        """)