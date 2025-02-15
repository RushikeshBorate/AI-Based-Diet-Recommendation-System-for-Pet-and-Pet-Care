#Handles User-Related Operations

from database.db_connection import get_connection

def register_user(name, email, pet_name, pet_age, pet_breed):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, pet_name, pet_age, pet_breed) VALUES (%s, %s, %s, %s, %s)",
                   (name, email, pet_name, pet_age, pet_breed))
    conn.commit()
    conn.close()