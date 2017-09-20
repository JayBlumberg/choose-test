import sqlite3
dbname = 'music.sqlite3'
conn = sqlite3.connect(dbname)
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Tracks ')
cur.execute('CREATE TABLE Tracks (Title TEXT, plays INTEGER)')
cur.execute('INSERT INTO Tracks (Title, plays) VALUES (?,?)',
	    ( 'My Way', 15))
cur.execute('INSERT INTO Tracks (Title, plays) VALUES (?,?)',
        ( 'Your Way', 25))
conn.commit()
print ('Tracks:')
cur.execute('SELECT Title, plays FROM Tracks')
for row in cur :
	print (row)
cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()
cur.close()
print ("Test successful")

