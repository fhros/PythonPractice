from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Funktio, joka hakee lentokentän tiedot tietokannasta
def hae_lentokentta(icao):
    yhteys = sqlite3.connect('airports.db')
    kursori = yhteys.cursor()
    kursori.execute("SELECT name, municipality FROM airports WHERE icao_code = ?", (icao,))
    rivi = kursori.fetchone()
    yhteys.close()
    if rivi:
        return {"ICAO": icao, "Name": rivi[0], "Municipality": rivi[1]}
    else:
        return None

# Reitti, joka käsittelee GET-pyynnön
@app.route('/kenttä/<string:icao>', methods=['GET'])
def kentta(icao):
    lentokentta = hae_lentokentta(icao)
    if lentokentta:
        return jsonify(lentokentta)
    else:
        return jsonify({"error": "Lentokenttää ei löydy"}), 404

if __name__ == '__main__':
    app.run(port=3000)
