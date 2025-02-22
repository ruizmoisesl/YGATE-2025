from flask import  render_template , Flask , Blueprint , current_app
import mysql.connector as MySQLdb
from routes.database import mysql

productosBP = Blueprint('productos', __name__)

@productosBP.route('/productos')
def productos():
    cursor = mysql.cursor()
    cursor.execute('SELECT ID_Producto,Precio_Base,Precio_Final,Stock,Color FROM Detalles_Producto')
    user = cursor.fetchall()
    cursor.close()
    cursor = mysql.cursor()
    cursor.execute('SELECT Nombre,Marca,Referencia FROM Productos')
    productos = cursor.fetchall()
    cursor.close()
    print(productos,"Productos")
    return render_template("productos.html",productos=zip(user,productos))
        


    
    