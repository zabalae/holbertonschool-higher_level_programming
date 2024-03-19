#!/usr/bin/python3
'''Script ttthat lists all cities from the database'''


import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM \
                   cities INNER JOIN states ON states.id=cities.state_id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
