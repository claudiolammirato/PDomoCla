import sqlite3
import csv
import StringIO

def sqlcsv():
	
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
	        data1.append(row[0]+"_"+row[1]+","+row[2]+","+row[3])
	        
	       

	#print data1
	out_file = open("static/output1.csv","w")
	out_file.write("Data, Hum, Temp\n")
	for row1 in data1:
		out_file.write(row1+"\n")
	out_file.close()
