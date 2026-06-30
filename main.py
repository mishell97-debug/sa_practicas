import os
import json

# Cambiado a formato .json para cumplir la Actividad 3
A = "datos_inv.json"

# Se añade 'codigo_barras' al inicio como parámetro obligatorio (Actividad 4)
def p_pro(codigo_barras, op, x, p, c, t):
    
    if op == 1:
        # VALIDACIÓN Y REGISTRO DE PRODUCTO
        if codigo_barras == "" or x == "" or p <= 0 or c < 0:
            print("Error: Datos inválidos.")
            return False
        
        # Financiero solicita que 'Tecnología' pague el 12% de IVA en lugar del 15% (Actividad 2)
        if t == "Tecnología":
            iva = p * 0.12
        else:
            iva = p * 0.15
            
        total_con_iva = p + iva
        
        if t == "Tecnología":
            p_final = total_con_iva - (total_con_iva * 0.10)
        else:
            p_final = total_con_iva
            
        # Estructura de datos para formato JSON (Actividad 3 y 4)
        nuevo_producto = {
            "codigo_barras": codigo_barras,
            "nombre": x,
            "precio": p,
            "stock": c,
            "categoria": t,
            "precio_final": p_final
        }
        
        # Leer datos existentes o iniciar lista vacía
        productos = []
        if os.path.exists(A):
            with open(A, "r") as f:
                try:
                    productos = json.load(f)
                except json.JSONDecodeError:
                    productos = []
                    
        productos.append(nuevo_producto)
        
        # Escritura estructurada en archivo JSON (Actividad 3)
        with open(A, "w") as f:
            json.dump(productos, f, indent=4)
            
        print("Producto guardado con éxito en formato JSON.")
        
    elif op == 2:
        # LECTURA Y DESPLIEGUE EN TABLA
        if not os.path.exists(A):
            print("No hay datos registrados.")
            return
        
        with open(A, "r") as f:
            try:
                productos = json.load(f)
            except json.JSONDecodeError:
                print("Error al leer el archivo JSON.")
                return
        
        print("----------------------------------------------------------------------")
        print("CÓDIGO | PROD | PRECIO | STOCK | CAT | PRECIO FINAL")
        print("----------------------------------------------------------------------")
        for prod in productos:
            # Reemplazo de variables crípticas por legibles para el reporte
            cb = prod["codigo_barras"]
            x1 = prod["nombre"]
            p1 = prod["precio"]
            c1 = prod["stock"]
            t1 = prod["categoria"]
            pf1 = prod["precio_final"]
            
            print(f"{cb} | {x1} | ${p1} | {c1} unidades | {t1} | ${pf1}")
            
            # Alerta exigida por control de calidad si el stock es menor a 5 (Actividad 1)
            if c1 < 5:
                print(f"   ⚠️ ALERTA: ¡El stock de '{x1}' es crítico! ({c1} unidades disponibles)")
                
        print("----------------------------------------------------------------------")

    elif op == 3:
        # SIMULACIÓN DE REPORTES
        if not os.path.exists(A):
            print("No hay datos para generar el reporte de IVA.")
            return
            
        with open(A, "r") as f:
            try:
                productos = json.load(f)
            except json.JSONDecodeError:
                return
        
        sumatoria = 0
        for prod in productos:
            precio_base = prod["precio"]
            # Ajuste de reporte financiero: IVA del 12% a tecnología y 15% al resto (Actividad 2)
            if prod["categoria"] == "Tecnología":
                iva_repetido = precio_base * 0.12
            else:
                iva_repetido = precio_base * 0.15
            sumatoria += iva_repetido
            
        print(f"Total de IVA acumulado en inventario: ${sumatoria:.2f}")

# Simulación de ejecución del programa actualizado
if __name__ == "__main__":
    print("--- SISTEMA DE INVENTARIO ACTUALIZADO V2.0 ---")
    
    # Se añade el string de código de barras al inicio en las llamadas (Actividad 4)
    # Cambié el stock de la Laptop a 4 para comprobar que la alerta funcione en consola (Actividad 1)
    p_pro("78912345", 1, "Laptop", 800.0, 4, "Tecnología")
    p_pro("78956789", 1, "Cuaderno", 2.50, 50, "Útiles")
    
    # Listar productos
    p_pro("", 2, "", 0, 0, "")
    
    # Ver reporte de IVA
    p_pro("", 3, "", 0, 0, "")
