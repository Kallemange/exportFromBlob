import fileManagement as fw
import pyodbc

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

    def execSQL(self):
        cursor = self.conn.cursor()
        fw.newDir('../../out')
        for tabell in self.config.tables:
            SQLStr = self.getSQLStr(tabell)
            cursor.execute(SQLStr)
            fw.writeToFile(cursor.fetchall(), tabell)
