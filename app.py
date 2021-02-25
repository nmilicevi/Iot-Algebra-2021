#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask_mysqldb import MySQL
from flask import request

mysql = MySQL()
app = Flask(__name__)


#MySQL configuration
app.config['MYSQL_USER'] = 'NinaUser'
app.config['MYSQL_PASSWORD'] = 'Nina123.'
app.config['MYSQL_DB'] = 'telemetryDB'
app.config['MYSQL_HOST'] ='localhost'
mysql.init_app(app)


books = [{'name': 'Snow White', 'author' : 'Grimm brothers'},
{'name' : "Alice's Addventures in Wonderlan", 'author' : 'Lewis Carrol'}
]

 

@app.route("/api/telemetry/", methods=['GET'])
def return_from_db():
conn = mysql.connect
cursor = conn.cursor()
From = request.args.get('From')
to = request.args.get("to")
if From is None or to is None:
cursor.execute("SELECT * FROM Measurements")
else:
cmd = "SELECT * FROM Measurements WHERE CreatedOn BETWEEN %s and %s"
params = (From, to)
cursor.execute(cmd, params)
rows = cursor.fetchall()
return jsonify({'telemetry': rows})

@app.route("/api/telemetry/", methods=['POST'])
def put_new_book():
new_data = request.get_json()
print(new_data)
conn = mysql.connect
cursor = conn.cursor()
cmd = "INSERT INTO Measurement ( MeasurementId,DeviceId, SensorName, SensorValue ,CreatedOn)"
values = "VALUES (NULL, %s , %s, %s , %s)"
cmd = cmd + values
# treba parsirati u datetime objekt
params = (new_data['DeviceId'], new_data['SensorName'], new_data['SensorValue'], new_data['CreatedOn'])
cursor.execute(cmd, params)
conn.commit()
cursor.close()
return "200"

 

@app.route("/", methods=['GET'])
def hello_world():
return "hello world"

 

 

if __name__ == "__main__":
app.run(host='0.0.0.0', port=80, debug=True)