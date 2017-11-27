import psycopg2
import os
from os import environ
from flask import Flask

app = Flask(__name__)



def setUp():
    return DatabaseLoader()

@app.route('/wine')
def index():
    return setUp()

class DatabaseLoader:
    #main function
    def __init__(self):
        server  = environ.get("server")
        user = environ.get("user")
        password = environ.get("password")
        dbname = environ.get("dbname")
        return self.setupDb(server, user, password, dbname)

    #takes the csv and inserts it into the db
    def setupDb(self, server, user, password, dbname):
        conn = psycopg2.connect("host=" + str(server) + " port='5432' dbname=" + str(dbname) + " user=" + str(user) + " password=" + str(password))
        cur = conn.cursor()

        # does table exist
        tb_exists = "select exists(select relname from pg_class where relname='" + "wine_reviews" + "')"
        cur.execute(tb_exists)
        execute = cur.fetchone()[0]
        if not execute:
            # make table
            cur.execute(
                'create table wine_reviews(country VARCHAR, designation VARCHAR, points INT, price VARCHAR, province VARCHAR, region_1 VARCHAR, region_2 VARCHAR, variety VARCHAR, winery VARCHAR);')
            conn.commit()
        # copy csv
        f = open(r'/opt/app-root/src/wineData.csv', 'r')
        cur.copy_from(f, "wine_reviews", sep=',')
        conn.commit()
        cur.execute("select * from wine_reviews limit 100;")
        data = cur.fetchone()[0]
        f.close()
        return data

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
