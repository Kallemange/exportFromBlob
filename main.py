import pyodbc
import os


#from wand.image import image
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=Solpmsql2;'
                      'Database=arvika_husar_20201110;'
                      'Trusted_Connection=yes;')

dir = 'dk_kamerabildserviceorderrad'
cursor = conn.cursor()
cursor.execute('SELECT top 1 DK_kamerabildId,radnr, bild, notering FROM ' + dir)
rows = cursor.fetchall()


try:
    os.mkdir(dir)
except Exception:
    pass

for row in rows:
    filnamn = dir +'/' + str(row.DK_kamerabildId)+"_" +str(row.radnr)
    print(row)
