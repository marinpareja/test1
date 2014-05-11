#! /usr/bin/env python
import mysql.connector
import csv

connection=mysql.connector.connect(host='db4free.net', user='sql238823', password ='nF2*sK7%', database='sql238823')
cursor=connection.cursor()

with open('municipios.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        if row[2] == 'false' and int(row[0]) == 41:
            data_provincia = {'Municipio' : row[4],
                              'Provincia' : int(row[0]),
                              'CP' : int(row[3])
                            }
                 
            # Put this through to SQL using an INSERT statement...
            add_provincia = ("INSERT INTO core_municipio" "(Municipio,Provincia_id,CP)" "VALUES (%(Municipio)s, %(Provincia)s, %(CP)s)")
            #update_provincia = ("""UPDATE core_provincia SET Provincia=%(Provincia)s WHERE id=%(id)s""")
    
            cursor.execute(add_provincia, data_provincia)
            #cursor.execute(update_provincia, data_provincia)
        
            
connection.commit()
cursor.close()
connection.close()