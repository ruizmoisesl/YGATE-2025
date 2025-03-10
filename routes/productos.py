from flask import  render_template , Flask , Blueprint , current_app, session
from database import iniciar_connection
from routes.login import login

productosBP = Blueprint('productos', __name__)
@productosBP.route('/productos')
def productos():
        datos_tienda = session.get('datos_tienda')
        nit = session.get('nit')
        conexion = iniciar_connection()
        cursor = conexion.cursor()
        print("Conexión exitosa",nit)
        
        cursor.execute('SELECT Productos.Nombre,Productos.Marca,Productos.Referencia,Detalles_Producto.ID_Producto,Detalles_Producto.Precio_Base,Detalles_Producto.Precio_Final,Detalles_Producto.Stock,Detalles_Producto.Color FROM Productos JOIN Detalles_Producto ON Productos.ID_Producto = Detalles_Producto.ID_Producto WHERE tienda = %s',(nit,))
        productos = cursor.fetchall()
        cursor.close()
        conexion.close()
        print(productos,"Productos")
        
        return render_template("productos.html",productos=productos, tienda= datos_tienda)
        

    
    