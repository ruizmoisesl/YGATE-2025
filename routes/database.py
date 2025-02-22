import mysql.connector as MySQLdb

try:
    mysql = MySQLdb.connect(
        host="bogk9mha8ehn5owk1qeo-mysql.services.clever-cloud.com",
        user="udq78qvouupy05hi",
        passwd="FjhgEsSoU9KepA4XgIxR",
        db="bogk9mha8ehn5owk1qeo"
    )
    
    
except MySQLdb.Error as e:
        print(f"Error al conectar: {e}")

cursor = mysql.cursor()