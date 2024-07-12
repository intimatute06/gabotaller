from funciones_productos import (Producto, cargar_productos_de_archivo, 
                                 guardar_productos_en_archivo, listar_productos, 
                                 buscar_por_marca, buscar_por_categoria, 
                                 buscar_por_precio_menor, editar_producto, 
                                 anadir_producto, eliminar_producto, ejecutar_archivo)

def principal():
    productos = cargar_productos_de_archivo("productos.json")

    while True:
        print("Elija una opción:")
        print("1. Listar Productos")
        print("2. Buscar Productos")
        print("3. Editar Productos")
        print("4. Agregar Productos")
        print("5. Eliminar Productos")
        print("6. Salir")
        opcion1 = int(input(">> "))

        if opcion1 == 1:
            listar_productos(productos)
        elif opcion1 == 2:
            print("Buscar por:")
            print("1. Marca")
            print("2. Categoría")
            print("3. Precio Menor de")
            opcion2 = int(input(">> "))
            if opcion2 == 1:
                marca = input("Ingrese la marca: ")
                buscar_por_marca(productos, marca)
            elif opcion2 == 2:
                categoria = input("Ingrese la categoría: ")
                buscar_por_categoria(productos, categoria)
            elif opcion2 == 3:
                precio_maximo = float(input("Ingrese el precio máximo: "))
                buscar_por_precio_menor(productos, precio_maximo)
        elif opcion1 == 3:
            indice = int(input("Ingrese el ID del producto que desea editar: "))
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            nueva_categoria = input("Ingrese la nueva categoría: ")
            nueva_marca = input("Ingrese la nueva marca: ")
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            editar_producto(productos, indice, nuevo_nombre, nueva_categoria, nueva_marca, nuevo_precio)
        elif opcion1 == 4:
            nombre = input("Ingrese el nombre: ")
            categoria = input("Ingrese la categoría: ")
            marca = input("Ingrese la marca: ")
            precio = float(input("Ingrese el precio: "))
            anadir_producto(productos, nombre, categoria, marca, precio)
        elif opcion1 == 5:
            indice = int(input("Ingrese el ID del producto que desea eliminar: "))
            eliminar_producto(productos, indice)
        elif opcion1 == 6:
            guardar_productos_en_archivo(productos, "productos.json")
            with open("productos.txt", 'w') as file:
                for prod in productos:
                    file.write(f"{prod.indice}\t\t{prod.nombre}\t\t{prod.categoria}\t\t{prod.marca}\t\t{prod.precio:.2f}\n")
            ejecutar_archivo("productos.txt")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

        respuesta = input("¿Desea elegir otra opción? (s/n): ")
        if respuesta.lower() != 's':
            guardar_productos_en_archivo(productos, "productos.json")
            with open("productos.txt", 'w') as file:
                for prod in productos:
                    file.write(f"{prod.indice}\t\t{prod.nombre}\t\t{prod.categoria}\t\t{prod.marca}\t\t{prod.precio:.2f}\n")
            ejecutar_archivo("productos.txt")
            break

if __name__ == "__main__":
    principal()
