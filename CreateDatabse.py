import sqlite3, csv

con = sqlite3.connect("EquivalentSeismic.db")
cur = con.cursor()
#cur.execute("CREATE TABLE zonecoefficient(zones, coefficients)")

# res = cur.execute("SELECT name FROM sqlite_master")
# print(res.fetchone())
with open('ZoneCoefficient.csv','r') as fin:
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['Districts'], i['Zone Coefficient']) for i in dr]

cur.executemany("INSERT INTO zonecoefficient (zones, coefficients) VALUES (?, ?);", to_db)
con.commit()