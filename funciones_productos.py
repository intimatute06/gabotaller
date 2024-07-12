import os
import json

class Producto:
    def __init__(self, nombre, categoria, marca, precio, indice):
        self.nombre = nombre
        self.categoria = categoria
        self.marca = marca
        self.precio = precio
        self.indice = indice

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'categoria': self.categoria,
            'marca': self.marca,
            'precio': self.precio,
            'indice': self.indice
        }

    @staticmethod
    def from_dict(data):
        return Producto(data['nombre'], data['categoria'], data['marca'], data['precio'], data['indice'])

def cargar_productos_de_archivo(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        data = json.load(file)
        return [Producto.from_dict(prod) for prod in data]

def guardar_productos_en_archivo(productos, filename):
    with open(filename, 'w') as file:
        json.dump([prod.to_dict() for prod in productos], file, indent=4)
    print(f"Productos guardados en {filename} exitosamente!")

def listar_productos(productos):
    print("Numero\tNombre\t\tCategoria\tMarca\t\tPrecio")
    for prod in productos:
        print(f"{prod.indice}\t\t{prod.nombre}\t\t{prod.categoria}\t\t{prod.marca}\t\t{prod.precio:.2f}")

def buscar_por_marca(productos, marca):
    print("Nombre\t\tCategoria\tMarca\t\tPrecio")
    encontrado = False
    for prod in productos:
        if prod.marca == marca:
            print(f"{prod.nombre}\t\t{prod.categoria}\t\t{prod.marca}\t\t{prod.precio:.2f}")
            encontrado = True
    if not encontrado:
        print("No existe ningun producto con esa marca")

def buscar_por_categoria(productos, categoria):
    print("Nombre\t\tCategoria\tMarca\t\tPrecio")
    encontrado = False
    for prod in productos:
        if prod.categoria == categoria:
            print(f"{prod.nombre}\t\t{prod.categoria}\t\t{prod.marca}\t\t{prod.precio:.2f}")
            encontrado = True
    if not encontrado:
        print("No existe ningun producto con esa categoria")

def buscar_por_precio_menor(productos, precio_maximo):
    print("Nombre\t\tCategoria\tMarca\t\tPrecio")
    encontrado = False
    for prod in productos:
        if prod.precio <= precio_maximo:
            print(f"{prod.nombre}\t\t{prod.categoria}\t\t{prod.marca}\t\t{prod.precio:.2f}")
            encontrado = True
    if not encontrado:
        print("No existe ningun producto con ese precio menor")

def editar_producto(productos, indice, nuevo_nombre, nueva_categoria, nueva_marca, nuevo_precio):
    for prod in productos:
        if prod.indice == indice:
            prod.nombre = nuevo_nombre
            prod.categoria = nueva_categoria
            prod.marca = nueva_marca
            prod.precio = nuevo_precio
            print("Producto editado exitosamente!")
            guardar_productos_en_archivo(productos, "productos.json")
            return
    print("No se encontró un producto con ese ID")

def anadir_producto(productos, nombre, categoria, marca, precio):
    max_indice = max([prod.indice for prod in productos], default=0) + 1
    productos.append(Producto(nombre, categoria, marca, precio, max_indice))
    print("Producto agregado exitosamente!")
    guardar_productos_en_archivo(productos, "productos.json")

def eliminar_producto(productos, indice):
    for i, prod in enumerate(productos):
        if prod.indice == indice:
            productos.pop(i)
            # Reasignar índices a los productos restantes
            for j in range(i, len(productos)):
                productos[j].indice -= 1
            print("Producto eliminado exitosamente!")
            guardar_productos_en_archivo(productos, "productos.json")
            return
    print("No se encontró un producto con ese ID")

def ejecutar_archivo(filename):
    if os.name == 'nt':  # Para Windows
        os.system(f"start {filename}")
    elif os.name == 'posix':  # Para Unix/MacOS
        os.system(f"open {filename}")
