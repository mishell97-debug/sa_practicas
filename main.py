# main.py - Orquestador y Flujo del Programa Principal
from inventario import registrar_producto, listar_productos, generar_reporte_iva

if __name__ == "__main__":
    print("--- SISTEMA DE INVENTARIO MODULAR Y LIMPIO V3.0 ---")
    
    # Invocaciones de prueba con código de barras obligatorio
    registrar_producto("78912345", "Laptop", 800.0, 3, "Tecnología")
    registrar_producto("78956789", "Cuaderno", 2.50, 20, "Útiles")
    
    # Despliegue de los subsistemas modulares
    listar_productos()
    generar_reporte_iva()
    
