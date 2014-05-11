#! /usr/bin/env python
import mysql.connector
import csv

connection=mysql.connector.connect(host='db4free.net', user='sql238823', password ='nF2*sK7%', database='sql238823')
cursor=connection.cursor()

row_reads = 0
db_duplicate = 0

with open('apellidos.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        row_reads = row_reads + 1
        idApellido = int(row[0])
        Apellido = row[1]

        if idApellido:
            # Put this through to SQL using an INSERT statement...
            add_apellido = ("INSERT INTO core_apellido" "(Apellido)" "VALUES (%(Apellido)s)")    
            data_apellido = {'Apellido' : Apellido}
    
            try:
                print 'Creando: %i, %s ' % (idApellido, Apellido)
                cursor.execute(add_apellido, data_apellido)
            
            except:
                print 'Existe:  %i, %s ' % (idApellido, Apellido)
                db_duplicate = db_duplicate + 1
                

connection.commit()
cursor.close()
connection.close()

print 'Apellidos creados: %i, Apellidos duplicados %i ' % ((row_reads - db_duplicate), db_duplicate)
