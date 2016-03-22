# coding: utf8

host = "***"
user = "***"
password = "***"
connect = FTP(host, user, password)
etat = connect.getwelcome()
print "etat connexion ftp ", etat
rep = connect.dir()
print rep
    
file = open(nom, 'rb')
connect.sendcmd('CWD www/exemple/son')
connect.storbinary('STOR ' + nom, file)
    
file.close()
println("debug file close")
connect.quit()
println("\nTerminé !")