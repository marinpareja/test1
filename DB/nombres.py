#! /usr/bin/env python
import mysql.connector
import csv

connection=mysql.connector.connect(host='db4free.net', user='sql238823', password ='nF2*sK7%', database='sql238823')
cursor=connection.cursor()

row_reads = 0
db_duplicate = 0

with open('nombres_hombres.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        row_reads = row_reads + 1
        idNombre = int(row[0])
        Nombre = row[1]

        if idNombre:
            # Put this through to SQL using an INSERT statement...
            add_Nombre = ("INSERT INTO core_nombre" "(Nombre)" "VALUES (%(Nombre)s)")    
            data_Nombre = {'Nombre' : Nombre}
    
            try:
                print 'Creando: %i, %s ' % (idNombre, Nombre)
                cursor.execute(add_Nombre, data_Nombre)
            
            except:
                print 'Existe:  %i, %s ' % (idNombre, Nombre)
                db_duplicate = db_duplicate + 1
        
with open('nombres_mujeres.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        idNombre = int(row[0])
        Nombre = row[1]

        if idNombre:
            # Put this through to SQL using an INSERT statement...
            add_Nombre = ("INSERT INTO core_nombre" "(Nombre)" "VALUES (%(Nombre)s)") 
            data_Nombre = {'Nombre' : Nombre}
    
            try:
                print 'Creando: %i, %s ' % (idNombre, Nombre)
                cursor.execute(add_Nombre, data_Nombre)
            except:
                print 'Existe:  %i, %s ' % (idNombre, Nombre)
                db_duplicate = db_duplicate + 1
                    
connection.commit()
cursor.close()
connection.close()

print 'Nombres creados: %i, Nombres duplicados %i ' % ((row_reads - db_duplicate), db_duplicate)
