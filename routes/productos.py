from flask import  render_template
import MySQLdb


try:
    mysql = MySQLdb.connect(
        host="bogk9mha8ehn5owk1qeo-mysql.services.clever-cloud.com",
        user="udq78qvouupy05hi",
        passwd="FjhgEsSoU9KepA4XgIxR",
        db="bogk9mha8ehn5owk1qeo"
    )
    print("Conexión exitosa")
except MySQLdb.Error as e:
    print(f"Error al conectar: {e}")

def productos():
    try:
        cursor = mysql.cursor()
        cursor.execute('SELECT ID_Producto,Precio_Base,Precio_Final,Stock,Color FROM Detalles_Producto')
        user = cursor.fetchall()
        cursor.close()
        cursor = mysql.cursor()
        cursor.execute('SELECT Nombre,Marca,Referencia FROM Productos')
        productos = cursor.fetchall()
        cursor.close()
        print(productos)
        return render_template("productos.html",productos=zip(user,productos))
    except Exception as e:
        return f"Error: {str(e)}"


