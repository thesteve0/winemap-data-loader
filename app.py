import psycopg2
import argparse

class DatabaseLoader():
    #main function
    def __init__(self):
        parser = argparse.ArgumentParser(description='postgresql database')
        parser.add_argument('--server', help='the postgreql ip address')
        parser.add_argument('--user', help='username of postgresql user')
        parser.add_argument('--password', help='user password for postgresql')
        parser.add_argument('--dbname',help='the name of the database')
        args = parser.parse_args()
        self.setupDb(args.server, args.user, args.password, args.dbname)

    #takes the csv and inserts it into the db
    def setupDb(self, server, user, password, dbname):
        conn = psycopg2.connect("host=" + server + " port='5432' dbname="+dbname+" user="+user+" password="+password)
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
        f.close()


if __name__ == '__main__':
    DatabaseLoader()