import time

def dohotelWork(taskname,parameter):
    if(taskname="wakeup"):
        sql = "SELECT firstname,lastname from Residents WHERE roomnumber ={0}".format(parameter)
        output = "{0} {1} in room {3} received a wakeupcall at"
    elif(taskname="breakfast"):
        sql = "SELECT firstname,lastname from Residents WHERE roomnumber ={0}".format(parameter)
        output = "{0} {1} in room {3} has been served breakfast at"
    else:
        sql = """SELECT roomnumber FROM Rooms
        LEFT JOIN Residents on Rooms.Roomnum = Residents.Roomnum
        WHERE Residents.firstname is null"""
        rooms = ', '.join()
        output = "Rooms {0} were cleaned at".format(rooms)
    print output+" " +str(time.time())
        
