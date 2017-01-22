import time
import sqlite3

dbcon = sqlite3.connect('cronhoteldb.db')
cursor = dbcon.cursor()

def dohoteltask(taskname,parameter):
    if(taskname=="wakeup"):
        sql = "SELECT FirstName,LastName from Residents WHERE RoomNumber=?"
        cursor.execute(sql,(parameter,))
        result = cursor.fetchone()+(parameter,)
        output = "{0} {1} in room {2} received a wakeup call at".format(*result) 
    elif(taskname=="breakfast"):
        sql = "SELECT FirstName,LastName from Residents WHERE RoomNumber=?"
        cursor.execute(sql,(parameter,))
        result = cursor.fetchone()+(parameter,)
        output = "{0} {1} in room {2} has been served breakfast at".format(*result)
    
    else:
        sql = """SELECT Rooms.RoomNumber FROM Rooms
        LEFT JOIN Residents on Rooms.RoomNumber = Residents.RoomNumber
		WHERE Residents.FirstName is null"""
        cursor.execute(sql)
        rooms = cursor.fetchall()
        roomsSplited = ', '.join([str(room[0]) for room in rooms])
        output = "Rooms {0} were cleaned at".format(roomsSplited)

    now = time.time()
    print output+" " +str(now)
    return now