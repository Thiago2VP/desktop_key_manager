import mariadb
import sys
import random
from dotenv import load_dotenv
from dotenv import dotenv_values
from datetime import datetime

# Load dotenv
load_dotenv()
env_values = dotenv_values(".env")

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user=env_values['DATABASE_USER'],
        password=env_values['DATABASE_PASSWORD'],
        host=env_values['DATABASE_HOST'],
        port=3306,
        database=env_values['DATABASE']

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

def slectData():
    words = []
    try:
        cur.execute("SELECT * FROM words")
        for (word) in cur:
            words.append([word[0], word[1], word[2], word[3], word[4]])
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    return words

def insertData(name="", login="", keyPass="", description=""):
    now = datetime.now()
    dt_string = now.strftime("%H%M%S")
    random_int = random.randint(100, 999)
    dt_string += str(random_int)
    dt_string = int(dt_string)
    try:
        cur.execute(f"INSERT INTO words (id, wordName, login, keyPass, wordDescription) VALUES ({dt_string}, '{name}', '{login}', '{keyPass}', '{description}')")
        conn.commit()
    except mariadb.Error as e:
        return f"Error connecting to MariaDB Platform: {e}"
    return "Sucesso"

def updateData(wordId=0, name="", login="", keyPass="", description=""):
    try:
        cur.execute(f"UPDATE words SET wordName = '{name}', login = '{login}', keyPass = '{keyPass}', wordDescription = '{description}' WHERE id = {wordId}")
        conn.commit()
    except mariadb.Error as e:
        return f"Error connecting to MariaDB Platform: {e}"
    return "Sucesso"

def deleteData(wordId=0):
    try:
        cur.execute(f"DELETE FROM words WHERE id = {wordId}")
        conn.commit()
    except mariadb.Error as e:
        return f"Error connecting to MariaDB Platform: {e}"
    return "Sucesso"

def selectOneData(name=""):
    words = []
    try:
        cur.execute(f"SELECT * FROM words WHERE wordName = '{name}'")
        for (word) in cur:
            words.append([word[0], word[1], word[2], word[3], word[4]])
    except mariadb.Error as e:
        return f"Error connecting to MariaDB Platform: {e}"
    return words
