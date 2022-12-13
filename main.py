# import Flask for instance
# import request for methods
# import jsonify for encoding python dictionaries into json strings
import sqlite3

from flask import Flask, request, jsonify

app = Flask(__name__)


# function to connect to database
def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("jetliners.sqlite")
    except sqlite3.Error as e:
        print(e)
    return conn


# #route and view functions

@app.route('/')
def index():
    return 'Welcome to Jetliner Inventory!'


jetliners_list = [
    {
        "id": 0,
        "type": "Airbus: 220",
        # "type_id": "0105",
        "origin": "Canada",
        "engines": 2,
        "first_flight": "2013",
        "service_entry": "2016",
        "in_production": "yes",
        # "in_service": 146,
        "inventory": 50
    },
    {
        "id": 1,
        "type": "Boeing 737",
        # "type_id": "2065",
        "origin": "USA",
        "engines": 2,
        "first_flight": "1967",
        "service_entry": "1968",
        "in_production": "yes",
        # "in_service": 7649,
        "inventory": 23
    },
    {
        "id": 2,
        "type": "Boeing 777",
        # "type_id": "6002",
        "origin": "USA",
        "engines": 2,
        "first_flight": "1994",
        "service_entry": "1995",
        "in_production": "yes",
        # "in_service": 1483,
        "inventory": 107
    },
    {
        "id": 3,
        "type": "Boeing 747",
        # "type_id": 7,
        "origin": "USA",
        "engines": 4,
        "first_flight": "1969",
        "service_entry": "1970",
        "in_production": "no",
        # "in_service": 146,
        "inventory": 82
    },
    {
        "id": 4,
        "type": "Bombardier CRJ100",
        # "type_id": 7,
        "origin": "Canada",
        "engines": 2,
        "first_flight": "1999",
        "service_entry": "2001",
        "in_production": "no",
        # "in_service": 146,
        "inventory": 8
    },
    {
        "id": 5,
        "type": "Airbus A340",
        # "type_id": 7,
        "origin": "Europe",
        "engines": 4,
        "first_flight": "1991",
        "service_entry": "1993",
        "in_production": "no",
        # "in_service": 146,
        "inventory": 12
    }
]


@app.route('/jetliners', methods=['GET', 'POST'])
def jetliners():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        if len(jetliners_list) > 0:
            return jsonify(jetliners_list)
        else:
            'Nothing Found', 404

    if request.method == 'POST':
        new_type = request.form['type']
        new_origin = request.form['origin']
        new_engines = request.form['engines']
        new_first_flight = request.form['first_flight']
        new_service_entry = request.form['service_entry']
        new_in_production = request.form['in_production']
        new_inventory = request.form['inventory']
        # id set to last index of list plus 1
        iD = jetliners_list[-1]['id'] + 1

        # create new object to store info

        new_obj = {
            "id": iD,
            "type": new_type,
            # "type_id": 7,
            "origin": new_origin,
            "engines": new_engines,
            "first_flight": new_first_flight,
            "service_entry": new_service_entry,
            "in_production": new_in_production,
            "inventory": new_inventory
            # "in_service": 146,
        }

        # append new object to list

        jetliners_list.append(new_obj)
        return jsonify(jetliners_list)


@app.route('/jetliner/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_jetliner(id):
    if request.method == 'GET':
        for jetliner in jetliners_list:
            if jetliner['id'] == id:
                return jsonify(jetliner)
            pass
    if request.method == 'PUT':
        for jetliner in jetliners_list:
            if jetliner['id'] == id:
                jetliner['type'] = request.form['type']
                jetliner['origin'] = request.form['origin']
                jetliner['engines'] = request.form['engines']
                jetliner['first_flight'] = request.form['first_flight']
                jetliner['service_entry'] = request.form['in_production']
                jetliner['in_production'] = request.form['type']
                jetliner['inventory'] = request.form['inventory']
                updated_jetliner = {
                    'id': id,
                    'type': jetliner['type'],
                    'origin': jetliner['origin'],
                    'engines': jetliner['engines'],
                    'first_flight': jetliner['first_flight'],
                    'service_entry': jetliner['service_entry'],
                    'in_production': jetliner['in_production'],
                    'inventory': jetliner['inventory']

                }
                return jsonify(updated_jetliner)
    if request.method == 'DELETE':
        for index, jetliner in enumerate(jetliners_list):
            if jetliner['id'] == id:
                jetliners_list.pop(index)
                return jsonify(jetliners_list)


# call main app.name method


if __name__ == '__main__':
    app.run()
