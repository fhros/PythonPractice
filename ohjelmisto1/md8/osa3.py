import mysql.connector
from geopy.distance import geodesic

def connect_to_database():
    conn = mysql.connector.connect(
        user="root",
        password="ideal",
        host="localhost",
        database="flight_game",
        collation = "utf8mb4_general_ci"
    )
    return conn

def get_airport_coordinates(icao_code):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s", (icao_code,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result
    else:
        return None

def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).kilometers

if __name__ == "__main__":
    icao1 = input("anna eka icao koodi: ")
    icao2 = input("anna toinen: ")

    coords1 = get_airport_coordinates(icao1)
    coords2 = get_airport_coordinates(icao2)

    if coords1 and coords2:
        distance = calculate_distance(coords1, coords2)
        print(f"{icao1} ja {icao2} väli o {distance:.2f} km.")
    else:
        print("ei löytyny toista tia molempia lentokentist")