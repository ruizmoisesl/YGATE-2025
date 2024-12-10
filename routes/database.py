import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user = '',
    password = '',
    port= 3306
    )

cursor = connection.cursor()