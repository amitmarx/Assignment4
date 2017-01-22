import os
import sqlite3
import imp
import atexit
import sys



def insert_TaskTimes(id, doEvery, numTimes, cursor):
    cursor.execute("INSERT INTO TaskTimes (TaskId, DoEvery, NumTimes) VALUES (?, ?, ?)", (id, doEvery, numTimes,))


def insert_Tasks(id, taskName, param, cursor):
    cursor.execute("INSERT INTO Tasks (TaskId, TaskName, Parameter) VALUES (?, ?, ?)", (id, taskName, param,))


def insert_Rooms(roomNumber, cursor):
    cursor.execute("INSERT INTO Rooms (RoomNumber) VALUES (?)", (roomNumber,))

def insert_Residents(roomNumber, firstName, lastName, cursor):
    cursor.execute("INSERT INTO Residents(RoomNumber, FirstName, LastName) VALUES (?, ?, ?)", (roomNumber, firstName, lastName,))

def main(args):
    inputFileName = args[1]
    #TODO CHANGE BACK
    dataBaseExisted = os.path.isfile('cronhoteldb.db')
    dbcon = sqlite3.connect('cronhoteldb.db')
    cursor = dbcon.cursor()
    with dbcon:
        if not dataBaseExisted:
            cursor.execute("CREATE TABLE TaskTimes(TaskId INTEGER PRIMARY KEY, DoEvery INTEGER NOT NULL,NumTimes INTEGER NOT NULL)")
            cursor.execute("CREATE TABLE Tasks(TaskId INTEGER PRIMARY KEY REFERENCES TaskTimes(TaskId), TaskName INTEGER NOT NULL, Parameter INTEGER)")
            cursor.execute("CREATE TABLE Rooms(RoomNumber INTEGER PRIMARY KEY)")
            cursor.execute("CREATE TABLE Residents(RoomNumber INTEGER NOT NULL REFERENCES Rooms(RoomNumber), FirstName TEXT NOT NULL, LastName TEXT NOT NULL)")
    with open(inputFileName) as inputFile:
        i = 0
        for line in inputFile:
            line = line.strip()
            listLine = line.split(",")
            if listLine[0] == "room":
                insert_Rooms(int(listLine[1]), cursor)
                if len(listLine) > 2:
                    insert_Residents(int(listLine[1]), listLine[2], listLine[3], cursor)
            else:
                if listLine[0] == "clean":
                    insert_Tasks(i, "clean", 0, cursor)
                    insert_TaskTimes(i, int(listLine[1]), int(listLine[2]), cursor)
                else:
                    insert_TaskTimes(i, int(listLine[1]), int(listLine[3]), cursor)
                    if listLine[0] == "breakfast":
                        insert_Tasks(i, "breakfast", int(listLine[2]), cursor)
                    else:
                        insert_Tasks(i, "wakeup", int(listLine[2]), cursor)
                i += 1
            dbcon.commit()


if __name__ == '__main__':
    main(sys.argv)

