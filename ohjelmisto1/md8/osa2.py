import mysql.connector

def connect_to_database():
    conn  = mysql.connector.connect(
        user="root",
        password="ideal",
        host="localhost",
        database="flight_game",
        collation="utf8mb4_general_ci"
    )
    return conn

def main():
    iso_country = input("anna maa koodi: ")

    try:
        conn = connect_to_database()
        with conn.cursor() as cur:
            cur.execute("SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type", (iso_country,))
            results = cur.fetchall()

            if results:
                for type, count in results:
                    print(f"maassa {iso_country} on {count} {type} lentokenttiä.")
            else:
                print("ei löydy täl maa koodil")
    except mysql.connector.Error as error:
        print(error)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()