from urllib2 import Request, urlopen, URLError

import xml.etree.ElementTree as ET

import MySQLdb.cursors


def latlon_from_gridref(s_gridref):
	request = Request('http://www.nearby.org.uk/api/convert.php?key=4a362f4dda121f&p=' + s_gridref + '&output=text')

	try:
		response = urlopen(request)
		alldata = response.read()
		geodata = alldata.split('\n')[3]

		latlon = geodata.split(',')

		lat = float(latlon[2])
		lon = float(latlon[3])

		return [lat, lon]


	except URLError, e:
	    return None




db = MySQLdb.connect(user="root",         # your username
                     db="mba")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM bothies WHERE latitude = 0 and longitude = 0 LIMIT 0,10")

# print all the first cell of all the rows
for row in cur.fetchall():
	i_row_id = row[0]
	s_gridref = row[4]
	d_lat_lon = latlon_from_gridref(s_gridref)

	if d_lat_lon is not None:
		# update back into db
		print "update: ", i_row_id, "with: ", d_lat_lon
		cur.execute("UPDATE bothies SET latitude=%s, longitude=%s WHERE id=%s",
			(d_lat_lon[0], d_lat_lon[1], i_row_id)
			)


db.commit()


db.close()
