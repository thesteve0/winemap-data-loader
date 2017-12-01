import psycopg2
from os import environ


class DatabaseLoader:
    # main function
    def __init__(self):
        server = environ.get("server")
        user = environ.get("user")
        password = environ.get("password")
        dbname = environ.get("dbname")
        self.setup_db(server, user, password, dbname)

    # takes the csv and inserts it into the db
    def setup_db(self, server, user, password, dbname):
        conn = psycopg2.connect("host=" + str(server) + " port='5432' dbname="
                                + str(dbname) + " user=" + str(user)
                                + " password=" + str(password))
        cur = conn.cursor()

        # does table exist
        tb_exists = "select exists(" \
                    "select relname from pg_class where relname='"\
                    + "wine-reviews" + "')"
        cur.execute(tb_exists)
        execute = cur.fetchone()[0]
        if not execute:
            # make table
            cur.execute(
                'create table wine-reviews('
                'country VARCHAR, '
                'designation VARCHAR, '
                'points INT, '
                'price VARCHAR, '
                'province VARCHAR, '
                'region_1 VARCHAR, '
                'region_2 VARCHAR, '
                'variety VARCHAR, '
                'winery VARCHAR);')
            conn.commit()
        # copy csv
        f = open(r'/wine-data.csv', 'r')
        cur.copy_from(f, "wine_reviews", sep=',')
        conn.commit()
        f.close()


if __name__ == '__main__':
    DatabaseLoader()
