from conexion import Conexion
from cliente import Cliente

class ClienteDAO:
    SELECCIONAR = "SELECT * FROM clienste ORDER BY id"
    INSERTAR = "INSERT INTO clienste(nombre, apellido, membresia) VALUES (%s, %s, %s)"
    ACTUALIZAR = "UPDATE clienste SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s"
    ELIMINAR = "DELETE FROM clienste WHERE id=%s"
    

    @classmethod
    def seleccionar(cls):
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f"Ocurrió un error al seleccionar clientes: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexion:
                Conexion.liberar_conexion(conexion)

    @classmethod 
    def insertar(cls,cliente):
        conexion=None
        try:
            conexion=Conexion.obtener_conexion()
            cursor=conexion.cursor()
            valores=(cliente.nombre,cliente.apellido,cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e :
            print(f"error al inserata un usuario :{e}")
        finally:
            if conexion is not None :
                cursor.close()
                Conexion.liberar_conexion(conexion)
                
    @classmethod
    def aculaizar(cls,cliente):
        conexion=None
        try:
            conexion=Conexion.obtener_conexion()
            cursor=conexion.cursor()
            valores=(cliente.nombre,cliente.apellido,cliente.membresia,cliente.id)
            cursor.execute(cls.ACTUALIZAR,valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e :
            print(f"ocurrio un error al actulizar un cliente :{e}")
        finally:
            if conexion is not None: 
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls,cliente):
        conexion=None
        try:
            conexion=Conexion.obtener_conexion()
            cursor=conexion.cursor()
            valores=(cliente.id,)
            cursor.execute(cls.ELIMINAR,valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"ocrrio un error al eliminar un cliente :{e}")
        finally:
            if conexion is not  None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == "__main__":
    #insertar cliente   
#    cliente1=Cliente(nombre="alejandra",apellido="tellez",membresia=300)
#    cñientes_insertados=ClienteDAO.insertar(cliente1)
#    print(f"clientes insertados _{cñientes_insertados}")

    #ACTULAIZAR CLIENTE 
#   cliente_actualizar=Cliente(2,"alexa","tellez",400)
#   clientes_actulaizados=ClienteDAO.aculaizar(cliente_actualizar)
#   print(f"clientes actualizadaso {clientes_actulaizados}")

    #eliminar cliente 
    cliente_eliminar=Cliente(id=2)
    eliminado_el_cloiente=ClienteDAO.eliminar(cliente_eliminar)
    print(f"se elimino el cliente de la base de datos :{eliminado_el_cloiente}")
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)
