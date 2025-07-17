import hashlib
import os
from db import get_connection

PEPPER = "SECRET_KEY"
  
def create_secure_password(password):
  salt = os.urandom(16)  
  iterations = 100_000
  hash_value = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8') + PEPPER.encode('utf-8'),  
        salt,
        iterations
  )  
  password_hash = salt + hash_value
  return password_hash 

def signup():
    conn = get_connection()
    cursor = conn.cursor()
    username = input("Choose a username: ")
    password = input("Choose a password: ")

    # Generate secure hash
    password_hash = create_secure_password(password)  

    # Split hash into components
    salt, key = password_hash[:16], password_hash[16:]
    hash_algo = "PBKDF2"
    iterations = 100_000

    # Convert bytes to hex strings for DB storage
    salt_hex = salt.hex()
    key_hex = key.hex()

    insert_sql = (
        "INSERT INTO users (username, password_hash, salt, "
        "hash_algo, iterations) "
        "VALUES (%s, %s, %s, %s, %s)"
    )
    try:
        cursor.execute(insert_sql, (
            username,
            key_hex,
            salt_hex,
            hash_algo,
            iterations
        ))
        conn.commit()
        print("Signup successful! Please login.")
    except Exception as e:
        print("Username already exists or error occurred.", e)
    finally:
        conn.close()

def login():
    conn = get_connection()
    cursor = conn.cursor()
    username = input("Username: ")
    password = input("Password: ")

    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    if not user:
        print("User not found or Invalid username.")
        conn.close()
        return None
    
    key_hex, salt_hex, hash_algo, iterations = user[2:6]
    salt = bytes.fromhex(salt_hex)
    key = bytes.fromhex(key_hex)

    # Recompute hash from user entered password  
    password_hash = hashlib.pbkdf2_hmac(
        'sha256',  # hardcoded to match signup
        password.encode('utf-8') + PEPPER.encode('utf-8'),
        salt,
        int(iterations)
    )
    if password_hash == key:
        print("Login successful!")
        conn.close()
        return user[0]
    else:
        print("Invalid credentials.")
        conn.close()
        return None