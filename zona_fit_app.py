from cliente_dao import ClienteDAO
from cliente import Cliente
print("**cliente zona fit (gym)**")
opcion=None
while opcion !=5 :
    print(f"""Menu:
          1.Listar clientes
          2.Agregar cliente
          3.Modificar cliente 
          4.Eliminar cliente 
          5.Salir """)
    opcion=int(input("escoge una opcion."))
    if opcion ==1:
        clientes=ClienteDAO.seleccionar()
        print("\n***listado de clientes***")
        for cliente in clientes:
            print(cliente)
    elif opcion ==2:
        nombre_var=input("escribe el nombre del nuevo cliente ") 
        apellido_var=input("escribe el apellido del del nuevo cliente ")
        membrecia_var=input("ingresa la membresia ")
        cliente =Cliente(nombre=nombre_var,apellido=apellido_var,membresia=membrecia_var)
        clientes_insertados=ClienteDAO.insertar(cliente)
        print(f"clientes insertados {clientes_insertados}")

    elif opcion==3:
        id_cliente_var=int(input("escribe el id del cliente a modificar "))
        nombre_var=input("escribe el nmombre")
        apellido_var=input("escribe el apellido")
        membrecia_var=input("escribe la membrescia ")
        cliente=Cliente(id_cliente_var,nombre_var,apellido_var,membrecia_var) 
        clientes_actualizado =ClienteDAO.aculaizar(cliente)
        print("cliente aculaizado")
    elif opcion==4:
        id_cliente_var=int(input("ingres el valor de id que vas a eliminar?"))
        cliente=Cliente(id=id_cliente_var)
        clientes_eliminados=ClienteDAO.eliminar(cliente)
        print("clienete eliminado")