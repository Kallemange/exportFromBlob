import os

def newDir(path):
    try:
        os.mkdir(path)
    except Exception:
        pass

def writeToFile(rows, tabell):
    #rows = cursor.fetchall()
    newDir('../../out/' +tabell)
    for row in rows:
        filnamn = tabell.strip() +'/' + str(row.DK_kamerabildId)+"_" +str(row.lopnr)
        with open('../../out/' +filnamn+ '.jpg', 'wb') as fil:
            fil.write(row.bild)

def readFromFile():
    pass
