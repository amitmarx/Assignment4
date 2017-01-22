import os
import sqlite3

dataBaseExists = os.path.isfile('cronhoteldb.db')
dbcon = sqlite3.connect('cronhoteldb.db')
cursor = dbcon.cursor()

def main():
    tasksLeft = tasksLeft()
    while(dataBaseExists and len(tasksLeft)>0):
        for task in range(0, len(tasksLeft)):
            (id, name, param, doEvery, numTimes, time) = tasksLeft[task]
            if (time<time.time()):
                thisTime = dohotelwork(name, param)
                tasksLeft[task] = (id, name, param, doEvery, numTimes, thisTime+doEvery)
                cursor.execute("""UPDATE TaskTimes SET NumTimes=? WHERE TaskId=?""", (numTimes-1, id,))
        tasksLeft = [i for i in tasksLeft if i[4] != 0]



def tasksLeft():
    cursor.execute("""SELECT Tasks.TaskId, Tasks.TaskName, Tasks.Parameter, TaskTimes.DoEvery, TaskTimes.NumTimes 0 from TaskTimes
    JOIN Tasks on TaskTimes.TaskId=Tasks.TaskId WHERE NumTimes>0""")
    result = cursor.fetchall()
    return result
