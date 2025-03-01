#Desarrolle un programa en Python que permita al usuario gestionar un inventario de productos. 
# El programa debe ofrecer diversas opciones para administrar los productos almacenados, 
# permitiendo añadir, buscar, eliminar, actualizar y filtrar productos según su categoría o precio. 
# Esta actividad está diseñada para que los estudiantes integren y apliquen sus conocimientos en el 
# manejo de cadenas de caracteres, arreglos, condicionales, y bucles en un contexto práctico 
# preparando el terreno para proyectos más complejos en el futuro.

import os
import time #Libreria para agregar pausas
def limpia_pantallas():
    os.system('cls' if os.name=='nt' else 'clear')
    
#Esta funcion nos ayudara a mostrar el menu de opciones al usuario.
def mostrar_menu_usuario():
    print("\n--Gestion de Inventario--")
    print("1. Agregar Productos")
    print("2. Buscar Productos por Nombre")
    print("3. Eliminar Productos")
    print("4. Editar Productos")
    print("5. Filtrar Productos por categoria")
    print("6. Filtrar productos por rango de precio")
    print("7. Mostrar productos ordenados alfabeticamente")
    print("8. Salir")

#definimos nuestra funcion como main para poder dar vida a nuestro programa.
def main():
    #Declaramos inventario como nuestra variable para poder usar en el ciclo while
    inventario=[]
    while True:
        #Llamamos a nuestra funcion mostrar menu para decir que trabajaremos con las opciones visualizadas.
        mostrar_menu_usuario()
        opcion=input("Seleccione una opcion: ")
        limpia_pantallas()
        if opcion == "1":
            agregar_productos(inventario)
            
        elif opcion =="2":
            buscar_productos(inventario)
            
        elif opcion =="3":
            eliminar_productos(inventario)
            
        elif opcion == "4":
            editar_productos(inventario)
            
        elif opcion == "5":
            filtrar_xcategoria(inventario)
            
        elif opcion == "6":
            filtrar_xprecio(inventario)
            
        elif opcion == "7":
            mostrar_productos_ol(inventario)
            
        elif opcion == "8":
            #En esta opciona usamos la funcion time.sleep(), para que el usuario pueda
            #ver el mensaje en el tiempo determinado, que vendria siendo 2 segundos, y asi cerrar el menu.
            print("Muchas gracias por tu tiempo.")
            time.sleep(2)
            break
        
#Funcion para agregar productos al inventario
def agregar_productos(inventario):
    limpia_pantallas()
    nombre=input("Nombre del producto: ").strip()
    precio=float(input("Precio del producto: "))
    categoria=input("Categoria del producto: ").strip()
    inventario.append({"nombre":nombre, "precio":precio, "categoria":categoria})
    print("Producto agregado con exito.")

#Funcion para buscar productos por su nombre.
def buscar_productos(inventario):
    limpia_pantallas()
    #Use el metodo .strip() para evitar problemas cuando el usuario escriba accidentalmente espacios adicionales.
    #Tambien use el metodo .lower() que me ayuda a convertir la cadena a minuscula, dando una comparacion igual entre mayuscula y minuscula.
    nombre=input("Ingresar el nombre del producto a buscar: ").strip()
    for producto in inventario:
        if producto["nombre"].lower()==nombre.lower():
            print("Producto encontrado con exito.")
        else:
            print("Producto no encontrado.")

#Funcion para eliminar productos
def eliminar_productos(inventario):
    limpia_pantallas()
    #Aqui luego de buscar el producto por su nombre, uso el procedimiento .remove
    #para poder eliminar el producto del sistema.
    nombre=input("Ingrese el nombre del producto a buscar: ").strip()
    for producto in inventario:
        if producto["nombre"].lower()== nombre.lower():
            inventario.remove(producto)
            print("Producto eliminado con exito.")
        else:
            print("Producto no encontrado.")

#fUNCION PARA EDITAR PRODUCTOS.
#En esta funcion usamos un ciclo for, para poder realizar los cambios necesarios, tanto del nombre, precio y categoria del producto
def editar_productos(inventario):
    limpia_pantallas()
    nombre=input("Ingrese el nombre del producto a editar: ").strip()
    for producto in inventario:
        if producto["nombre"].lower()== nombre.lower():
            print(f"Producto actual: {producto}")
            producto["nombre"]=input("Nuevo nombre: ") or producto["nombre"]
            try:
                nuevo_precio=input("Nuevo precio: ")
                if nuevo_precio:
                    producto["precio"]=float(nuevo_precio)
            except ValueError:
                print("Precio invalido.\nPrecio anterior en uso.")
            producto["categoria"]=input("Nueva categoria: ") or producto["categoria"]
            print("Producto actualizado con exito.")
            return
    print("Producto no encontrado.")

#Funcion para filtrar todos los productos por la categoria.
#Mi variable filtrados, nos ayuda a encontrar todos los productos que esten guardados
#En esa misma categoria, y luego se presenta x pantalla el producto.
def filtrar_xcategoria(inventario):
    limpia_pantallas()
    categoria=input("Ingrese la categoria a filtrar: ").strip()
    filtrados=[p for p in inventario if p["categoria"].lower()==categoria.lower()]
    if filtrados:
        print("Productos en la categoria: \n", filtrados)
    else:
        print("No hay productos en la categoria.")

#Funcion para filtrar todos los productos que se encuentren en el rango del precio solicitado
#Desde el precio minimo hasta el precio maximo
#La variable filtrados nos ayuda a encontrar todos los productos que esten en este rango.
def filtrar_xprecio(inventario):
    limpia_pantallas()
    try:
        min_precio=float(input("Ingrese el precio minimo: "))
        max_precio=float(input("Ingrese el precio maximo: "))
        filtrados=[p for p in inventario if min_precio<= p["precio"]<=max_precio]
        if filtrados:
            print("Productos en el rango del precio: \n",filtrados)
        else:
            print("No hay productos determinados en el rango del precio solicitado.")
    except ValueError:
        print("Entrada invalida.\n Intente de nuevo.")


#Funcion para mostrar productos de manera ordenada.
#Mi variable ol significa productos ordenados, la usaremos con la funcion sorted y key=lambda x:x["nombre"].lower() 
#para asegurar que la comparacion sea insensible a las mayusculas y minusculas, si hay productos los muestra en orden 
#Si el inventario esta vacio lo informa al usuario.
def mostrar_productos_ol(inventario):
    if inventario:
        ol=sorted(inventario, key=lambda x:x["nombre"].lower())
        print("Lista de productos ordenados: ")
        for p in ol:
            print(p)
    else:
        print("El inventario esta vacio.")


#Punto de entrada del programa.
if __name__=="__main__":
    main()


 
