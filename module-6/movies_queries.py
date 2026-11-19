
import mysql.connector
from mysql.connector import errorcode
from dotenv import dotenv_values

# Read database login information from .env
secrets = dotenv_values("../module-5/.env")

config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

db = None

try:
    # Connect to the movies database
    db = mysql.connector.connect(**config)
    # Query 1: Display all studio records
    cursor = db.cursor()
    cursor.execute("SELECT * FROM studio")
    studios = cursor.fetchall()

    print("\n-- DISPLAYING Studio RECORDS --")
    for studio in studios:
        print("Studio ID: {}".format(studio[0]))
        print("Studio Name: {}\n".format(studio[1]))
        
            # Query 2: Display all genre records
    cursor.execute("SELECT * FROM genre")
    genres = cursor.fetchall()

    print("\n-- DISPLAYING Genre RECORDS --")
    for genre in genres:
        print("Genre ID: {}".format(genre[0]))
        print("Genre Name: {}\n".format(genre[1]))
        
            # Query 3: Display films under two hours
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    films = cursor.fetchall()

    print("\n-- DISPLAYING Short Film RECORDS --")
    for film in films:
        print("Film Name: {}".format(film[0]))
        print("Runtime: {}\n".format(film[1]))
        
            # Query 4: Display film names and directors
    cursor.execute(
        "SELECT film_name, film_director FROM film "
        "ORDER BY film_director"
    )
    directors = cursor.fetchall()

    print("\n-- DISPLAYING Director RECORDS in Order --")
    for director in directors:
        print("Film Name: {}".format(director[0]))
        print("Director: {}\n".format(director[1]))
    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(
        config["user"], config["host"], config["database"]
    ))

    input("\n\nPress Enter to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

finally:
    if db is not None and db.is_connected():
        db.close()

