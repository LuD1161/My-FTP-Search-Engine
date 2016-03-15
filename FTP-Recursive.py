import ftplib, re, ftputil, dbm
from ftputil import FTPHost

f = raw_input("Enter FTP address to search : ")
searchterm = raw_input("Enter the string to search : ")

user = raw_input("Enter Username (If Needed else Leave it Blank)")
passw = raw_input("Enter Password (If Needed else Leave it Blank)")
if user == "":
	user="anonymous"
if passw == "":
	passw="anonymous@"

ftp = ftputil.FTPHost(f,user,passw)
names = ftp.listdir(ftp.curdir)
fileList = []
count = 0
filecount = 0
rx = re.compile(searchterm,re.IGNORECASE)

try:
	recursive = ftp.walk(ftp.curdir,topdown=True,onerror=None)
	for root,dirs,files in recursive:
		for name in dirs:
			filecount=filecount+1
			m=rx.search(name)
			if m:
				dest=ftp.path.join(root,name)
				print('Found at : '+dest[1:])
				count=count+1


		if (count==0):
		  for name in files:
				  m=rx.search(name,re.IGNORECASE)
				  if m:
					  dest=ftp.path.join(root,name)
					  print('Found at : '+dest[1:])
					  count=count+1



except Exception as e:
   print ("Error:occurred",e)

print("Total Files Found "+f+" are "+str(count))
ftp.close()
