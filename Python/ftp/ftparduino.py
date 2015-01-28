import pysftp

srv = pysftp.Connection(host="192.168.1.101", username="root",
password="arduino")

# Get the directory and file listing
with srv.cd('..'):     # now in ./static
    	srv.chdir('mnt')      
	srv.chdir('sdb1')
	#data = srv.listdir()
	srv.get('test.db', preserve_mtime=True)

# Closes the connection
srv.close()

# Prints out the directories and files, line by line
#for i in data:
#    print i
