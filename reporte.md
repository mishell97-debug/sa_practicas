# Reporte de Deuda Técnica y Adaptabilidad del Software

**Asignatura:** Sistemas Ágiles
**Integrantes:** Andrea Mishell Galeano Jaramillo (Trabajo Individual)
**Fecha:** [30/06/2026]

---

## 1. Diagnóstico de Calidad (Código Legacy)
1. **Problema 1:** Función Gigante / Monolítica (`p_pro`). Afecta desde la línea 12 a la 79, ya que mezcla la lógica de validación, cálculo, presentación y escritura en archivos en un solo bloque.
2. **Problema 2:** Código Duplicado / Hardcoding. El cálculo del IVA del 15% se repite textualmente tanto en el registro de productos (línea 19) como en el reporte acumulado (línea 66).
3. **Problema 3:** Nombres Crípticos de Variables. Uso de variables poco legibles como `A`, `op`, `x`, `p`, `c`, `t`, `x1`, `p1`, lo cual dificulta la comprensión del código.

## 2. Mapeo de Dificultades para la Evolución (Evidencia Git)
* ### Rama: `cambio-impuesto` (Efectuado en mi rama actual)
  **Impacto encontrado:** Modificar el impuesto requirió alterar dos secciones de código distintas debido a que el valor del 15% estaba duplicado (hardcoded). El código opuso resistencia porque un cambio simple obligó a revisar múltiples bloques condicionales.

* ### Rama: `cambio-json`
  **Impacto encontrado:** Se rompió toda la arquitectura de entrada/salida de datos. Al cambiar el formato plano por JSON, las funciones de formateo mediante strings y splits de comas quedaron obsoletas, requiriendo reescribir por completo la lógica de las opciones 1, 2 y 3.

* ### Rama: `codigo-barras`
  **Impacto encontrado:** Insertar un parámetro al inicio de la estructura rompió la firma de la función principal. Esto obligó a modificar todos los puntos de llamada del programa simulado (líneas 74-79) e invalidó los registros preexistentes en la base de datos de persistencia.

## 3. Propuesta de Refactorización Inicial
1. Aplicar el Principio de Responsabilidad Única (SRP) dividiendo la función gigante en funciones independientes: `validar_producto()`, `calcular_iva()`, `guardar_base_datos()` y `mostrar_tabla()`.
2. Reemplazar los nombres crípticos por variables auto-explicativas (ej. cambiar `x` por `nombre_producto`, `p` por `precio_base`).
3. Crear una constante global o un archivo de configuración para los impuestos (ej. `IVA_GENERAL = 0.15`), eliminando los valores quemados en el código.

## 4. Conclusiones del Equipo
**Porcentaje estimado de deuda técnica en el script original (0% al 100%):** 80%
**Reflexión ágil:** Un software rígido y con alta deuda técnica frena drásticamente la velocidad de entrega porque cualquier requerimiento pequeño genera un "efecto dominó" de fallos imprevistos, obligando al desarrollador a destinar tiempo valioso a reparar lo existente en lugar de construir nuevo valor en el Sprint.