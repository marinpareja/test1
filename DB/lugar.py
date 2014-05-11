#! /usr/bin/env python
import mysql.connector
import csv

connection=mysql.connector.connect(host='db4free.net', user='sql238823', password ='nF2*sK7%', database='sql238823')
cursor=connection.cursor()

row_reads = 0
db_duplicate = 0

with open('lugar.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        row_reads = row_reads + 1
        idLugar = int(row[0])
        Municipio = row[2]
        Lugar = row[2]
        URL = row[3]

        if idLugar:
            # Put this through to SQL using an INSERT statement...
            add_apellido = ("INSERT INTO core_lugar" "(Lugar, Municipio, URL)" "VALUES (%(Lugar)s, %(Municipio)s, %(URL)s)")    
            data_apellido = {'Lugar' : Lugar, 'Municipio' : Municipio, 'URL' : URL}
    
            try:
                print 'Creando: %i, %s - %s' % (idLugar, Lugar, URL)
                cursor.execute(add_apellido, data_apellido)
            
            except:
                print 'Existe:  %i, %s - %s' % (idLugar, Lugar, URL)
                db_duplicate = db_duplicate + 1
                

connection.commit()
cursor.close()
connection.close()

print 'Lugares creados: %i, Lugares duplicados %i ' % ((row_reads - db_duplicate), db_duplicate)
