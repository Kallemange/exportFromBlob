import pyodbc
import os


#from wand.image import image
class Config():
    def __init__(self):
        with open('config.txt','r') as file:
            content = file.readlines()
            self.server = content[0].strip()
            self.database = content[1].strip()
            self.tables = content[2].split()
    def tostr(self):
        return 'Driver={SQL Server};Server='+self.server +';Database='+self.database +';Trusted_Connection=yes;'

def getSQLStr(tabell):
    tabell = tabell.strip()
    topX = ' top 10 '
    if (tabell.lower() == 'dk_kamerabildbesiktning'):
        return ('SELECT' +topX+ ' DK_kamerabildId,lopnr, bild, notering FROM ' + tabell)

    elif(tabell.lower() == 'dk_kamerabildbesiktrad'):
        return 'SELECT' +topX+ ' DK_kamerabildId,radlopnr AS lopnr, bild, notering FROM ' + tabell

    elif(tabell.lower() == 'dk_kamerabildserviceorderrad'):
        return 'SELECT' +topX+ ' DK_kamerabildId,radnr lopnr, bild, notering FROM ' + tabell


def execSQL(config, conn):
    cursor = conn.cursor()
    for tabell in config.tables:
        SQLStr = getSQLStr(tabell)
        cursor.execute(SQLStr)
        rows = cursor.fetchall()
        for row in rows:
            print(str(row.DK_kamerabildId) + ", " + str(row.lopnr) + ", " + row.notering)


def main():
    config = Config()
    conn = pyodbc.connect(config.tostr())

    execSQL(config, conn)
    try:
        os.mkdir(dir)
    except Exception:
        pass

    #for row in rows:
    #    filnamn = dir +'/' + str(row.DK_kamerabildId)+"_" +str(row.radnr)
        #print(row)

main()
