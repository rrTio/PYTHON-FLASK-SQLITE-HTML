from flask import Flask, render_template, request, make_response
import sqlite3

HOST_NAME = "localhost"
HOST_PORT = 80
DBFILE = "Test App/Registration.db"
app = Flask(__name__)

def getusers():
  conn = sqlite3.connect(DBFILE)
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM `pydb`")
  results = cursor.fetchall()
  conn.close()
  return results

@app.route("/")
def index():
  users = getusers()
  return render_template("users.html", usr=users)

if __name__ == "__main__":
  app.run(HOST_NAME, HOST_PORT)