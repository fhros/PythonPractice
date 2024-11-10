from collections import OrderedDict
from flask import Flask, Response
import mysql.connector
import json

app = Flask(__name__)

def hae_lentokentta(icao):
    try:
        conn = mysql.connector.connect(
            user="root",
            password="ideal",
            host="localhost",
            database="flight_game",
            collation="utf8mb4_general_ci"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT name, municipality FROM airport WHERE ident = %s", (icao,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return OrderedDict([("ICAO", icao), ("Name", row[0]), ("Municipality", row[1])])
        else:
            return None
    except mysql.connector.Error as e:
        print("Virhe tietokantayhteydessä:", e)
        return None

@app.route('/kenttä/<string:icao>', methods=['GET'])
def kentta(icao):
    lentokentta = hae_lentokentta(icao)
    if lentokentta:
        return Response(json.dumps(lentokentta), mimetype='application/json')
    else:
        return Response(json.dumps({"error": "ei löytyny lentokenttää"}), mimetype='application/json')

if __name__ == '__main__':
    app.run(port=3000)
