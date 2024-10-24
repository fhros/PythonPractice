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
    icao_code = input("anna icao koodi: ")

    try:
        conn = connect_to_database()
        with conn.cursor() as cur:
            cur.execute("SELECT name FROM airport WHERE ident = %s", (icao_code,))
            result = cur.fetchone()

            if result:
                print(f"lentokentän nimi: {result[0]}")
            else:
                print("ei löydy täl ICAO-koodil")
    except (Exception, mysql.connector.Error) as error:
        print(error)

if __name__ == "__main__":
    main()