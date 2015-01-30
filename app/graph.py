import matplotlib.pyplot as plt
import sqlite3 as lite
import sys
from datetime import time, datetime

def graph():
    con = lite.connect('test.db')

    with con:    
        
        cur = con.cursor()    
        cur.execute("SELECT * FROM Temp")

        rows = cur.fetchall()
        y=[]
        z=[]
        x=[]

        #print len(rows)

        for row in rows:
            y.append(row[3])
            x.append(datetime.strptime(row[1], '%H:%M:%S')) #%H:%M:%S
            z.append(row[2])

        x2h=[]
        y2h=[]
        z2h=[]

        for num in range(len(rows)-20,len(rows)):
        	
            x2h.append(x[num])
            y2h.append(y[num])
            z2h.append(z[num])
        

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x2h, y2h, '-', label = 'Temperature')
    ax.plot(x2h, z2h, '-r', label = 'Humidity')
    ax2 = ax.twinx()
    ax2.plot(x2h, z2h, '-r', label = 'Humidity')
    ax.legend(loc=0)
    ax.grid()
    ax.set_xlabel("Time")
    ax2.set_ylabel(r"Humidity (%)")
    ax.set_ylabel(r"Temperature ($^\circ$C)")
    ax2.set_ylim(0, 100)
    ax.set_ylim(-10,35)
    plt.savefig('static/temperature/temperature.jpg')
    #plt.show()