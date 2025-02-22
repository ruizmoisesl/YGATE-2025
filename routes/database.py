import mysql.connector

connection = mysql.connector.connect(
        host="bogk9mha8ehn5owk1qeo-mysql.services.clever-cloud.com",
        user="udq78qvouupy05hi",
        passwd="FjhgEsSoU9KepA4XgIxR",
        db="bogk9mha8ehn5owk1qeo"
    )

cursor = connection.cursor()