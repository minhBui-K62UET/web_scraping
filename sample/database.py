import mysql.connector


def create_database(db_name):
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS %s" % db_name)


def use_database(db_name):
    my_cursor.execute("USE %s" % db_name)


def create_table(tb_name):
    my_cursor.execute("CREATE TABLE IF NOT EXISTS %s (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), des TEXT, url VARCHAR(255))" % tb_name)

def insert_data(tb_name, val):
    my_cursor.execute("INSERT INTO %s (title, des, url) VALUES ('%s', '%s', '%s')" % (tb_name, val['title'], val['description'], val['url']))


def show_data(tb_name):
    my_cursor.execute("SELECT * FROM %s" % tb_name)


def fetch_data():
    my_cursor.fetchall()


def commit_db():
    my_db.commit()


def fetch_data():
    return my_cursor.fetchall()


my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
)

my_cursor = my_db.cursor()

