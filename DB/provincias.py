#! /usr/bin/env python
import mysql.connector
import csv

connection=mysql.connector.connect(host='db4free.net', user='sql238823', password ='nF2*sK7%', database='sql238823')
cursor=connection.cursor()

row_reads = 0
db_duplicate = 0

with open('provincias.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        row_reads = row_reads + 1
        iProvincia = int(row[0])
        value = row[1]

        # Put this through to SQL using an INSERT statement...
        add_provincia = ("INSERT INTO core_provincia" "(id, Provincia)" "VALUES (%(id)s, %(Provincia)s)")
        update_provincia = ("""UPDATE core_provincia SET Provincia=%(Provincia)s WHERE id=%(id)s""")

        data_provincia = {'id' : iProvincia,'Provincia' : value}
        try:      
            print 'Creando: %i, %s ' % (iProvincia, value)        
            cursor.execute(add_provincia, data_provincia)
            
        except:
            db_duplicate = db_duplicate + 1
            print 'Existe:  %i, %s ' % (iProvincia, value)
            cursor.execute(update_provincia, data_provincia)
        
            
connection.commit()
cursor.close()
connection.close()

print 'Provincias creadas: %i, Provincias actualizadas %i ' % ((row_reads - db_duplicate), db_duplicate)
