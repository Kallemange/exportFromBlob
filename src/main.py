import pyodbc
import os

class Config:
    def __init__(self):
        with open('../config.txt','r') as file:
            content = file.readlines()
            self.server = content[0].strip()
            self.database = content[1].strip()
            self.tables = content[2].split()
    def tostr(self):
        return 'Driver={SQL Server};Server='+self.server +';Database='+self.database +';Trusted_Connection=yes;'
## TODO:
#Generalisera skript
class SQLExporter:

    def __init__(self, config):
        self.config = config
        self.conn = pyodbc.connect(self.config.tostr())

    def getSQLStr(self, tabell):
        tabell = tabell.strip()
        topX = ' top 1 '
        if (tabell.lower() == 'dk_kamerabildbesiktning'):
            return ('SELECT' +topX+ ' DK_kamerabildId,lopnr, bild, notering FROM ' + tabell)

        elif(tabell.lower() == 'dk_kamerabildbesiktrad'):
            return 'SELECT' +topX+ ' DK_kamerabildId,radlopnr AS lopnr, bild, notering FROM ' + tabell

        elif(tabell.lower() == 'dk_kamerabildserviceorderrad'):
            return 'SELECT' +topX+ ' DK_kamerabildId,radnr lopnr, bild, notering FROM ' + tabell

    def newDir(self, path):
        try:
            os.mkdir(path)
        except Exception:
            pass

    def execSQL(self): #config, conn):
        cursor = self.conn.cursor()
        self.newDir('../../out')
        for tabell in self.config.tables:
            SQLStr = self.getSQLStr(tabell)
            cursor.execute(SQLStr)
            rows = cursor.fetchall()
            self.newDir('../../out/' +tabell)
            for row in rows:
                #print(str(row.DK_kamerabildId) + ", " + str(row.lopnr) + ", " + str(row.notering))
                filnamn = tabell.strip() +'/' + str(row.DK_kamerabildId)+"_" +str(row.lopnr)
                with open('../../out/' +filnamn+ '.jpg', 'wb') as fil:
                    fil.write(row.bild)



def main():
    config = Config()
    exporter = SQLExporter(config)
    exporter.execSQL()
    print('klar')


if __name__ == "__main__":
    main()
