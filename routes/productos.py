from flask import  render_template , Flask , Blueprint , current_app, session
from database import iniciar_connection

productosBP = Blueprint('productos', __name__)
@productosBP.route('/productos')
def productos():
        datos_tienda = session.get('datos_tienda')
        conexion = iniciar_connection()
        cursor = conexion.cursor()
        print("Conexión exitosa")

        cursor.execute('SELECT ID_Producto,Precio_Base,Precio_Final,Stock,Color FROM Detalles_Producto')
        user = cursor.fetchall()
        cursor.execute('SELECT Nombre,Marca,Referencia FROM Productos')
        productos = cursor.fetchall()
        cursor.close()
        conexion.close()
        print(productos,"Productos")
        
        return render_template("productos.html",productos=zip(user,productos), tienda= datos_tienda)
        

    
    