#!/usr/bin/python3
'''Script that takes in the name of a state as an argument
and lists all cities of that state'''


import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities INNER JOIN states \
                   ONN states.id LIKE cities.state_id WHERE \
                   states.name LIKE BINARY '{}' ORDER BY \
                   cities.id".format(sys.argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
