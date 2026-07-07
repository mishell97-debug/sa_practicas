# inventario.py - Capa de Lógica de Negocio
import os
import json
from config import ARCHIVO_BASE_DATOS, IVA_GENERAL, IVA_TECNOLOGIA, DESCUENTO_TECNOLOGIA

def cargar_productos():
    """Carga los productos desde el archivo estructurado JSON."""
    if not os.path.exists(ARCHIVO_BASE_DATOS):
        return []
    try:
        with open(ARCHIVO_BASE_DATOS, "r") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        return []

def guardar_productos(productos):
    """Guarda de forma segura los productos en el almacenamiento persistente."""
    with open(ARCHIVO_BASE_DATOS, "w") as archivo:
        json.dump(productos, archivo, indent=4)

def calcular_iva(precio, categoria):
    """Calcula el impuesto correspondiente según regulaciones financieras."""
    if categoria == "Tecnología":
        return precio * IVA_TECNOLOGIA
    return precio * IVA_GENERAL

def calcular_precio_final(total_con_iva, categoria):
    """Aplica descuentos comerciales si el producto es tecnológico."""
    if categoria == "Tecnología":
        return total_con_iva - (total_con_iva * DESCUENTO_TECNOLOGIA)
    return total_con_iva

def verificar_alerta_stock(nombre, stock):
    """Regla de Control de Calidad: Alerta de existencias mínimas."""
    if stock < 5:
        print(f"   ⚠️ ALERTA: ¡El stock de '{nombre}' es crítico! ({stock} unidades disponibles)")

def registrar_producto(codigo_barras, nombre, precio, stock, categoria):
    """Valida, procesa y almacena un nuevo elemento en el inventario."""
    if not codigo_barras or not nombre or precio <= 0 or stock < 0:
        print("Error: Datos inválidos.")
        return False
        
    iva = calcular_iva(precio, categoria)
    total_con_iva = precio + iva
    precio_final = calcular_precio_final(total_con_iva, categoria)
    
    nuevo_producto = {
        "codigo_barras": codigo_barras,
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "categoria": categoria,
        "precio_final": precio_final
    }
    
    productos = cargar_productos()
    productos.append(nuevo_producto)
    guardar_productos(productos)
    print(f"Producto '{nombre}' guardado con éxito.")
    return True

def listar_productos():
    """Genera la visualización tabular legible de existencias."""
    productos = cargar_productos()
    if not productos:
        print("No hay datos registrados.")
        return
        
    print("-" * 75)
    print(f"{'CÓDIGO':<12} | {'PRODUCTO':<15} | {'PRECIO':<8} | {'STOCK':<10} | {'CAT':<12} | {'PRECIO FINAL'}")
    print("-" * 75)
    for prod in productos:
        print(f"{prod['codigo_barras']:<12} | {prod['nombre']:<15} | ${prod['precio']:<7.2f} | {prod['stock']:<6} unid. | {prod['categoria']:<12} | ${prod['precio_final']:.2f}")
        verificar_alerta_stock(prod['nombre'], prod['stock'])
    print("-" * 75)

def generar_reporte_iva():
    """Genera reportes de acumulación impositiva sin duplicar código."""
    productos = cargar_productos()
    if not productos:
        print("No hay datos para generar el reporte.")
        return
        
    total_iva_acumulado = 0
    for prod in productos:
        total_iva_acumulado += calcular_iva(prod["precio"], prod["categoria"])
        
    print(f"Total de IVA acumulado en inventario: ${total_iva_acumulado:.2f}")