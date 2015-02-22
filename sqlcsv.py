import sqlite3
import csv
import StringIO
import datetime

def sqlcsv():
	pass
	conn = sqlite3.connect("test.db")
	conn.text_factory = str ## my current (failed) attempt to resolve this
	cur = conn.cursor()
	data = cur.execute("SELECT * FROM Temp")

	#data = cur.execute("SELECT * FROM Temp")


	with open('static/output.csv', 'wb') as f:
	    writer = csv.writer(f)
	    #writer.writerow(['Column 1', 'Column 2','Column 3','Column 4'])
	    writer.writerows(data)

	data1 = []
	

	for row in csv.reader(open('static/output.csv'),delimiter=","):
		dt = datetime.datetime.strptime(row[0], '%Y-%m-%d').strftime('%Y/%m/%d')
		data1.append(dt+" "+row[1]+","+row[2]+","+row[3])
	        
	       

	#print data1
	out_file = open("static/output1.csv","w")
	out_file.write("Data, Humidity, Temperature\n")
	for row1 in data1:
		out_file.write(row1+"\n")
	out_file.close()
