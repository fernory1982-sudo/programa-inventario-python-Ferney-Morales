# Matriz de inventario: [Código, Nombre, Stock Actual, Stock Mínimo]
inventario = [
    ["A001", "Laptop Dell", 15, 25],
    ["A002", "Mouse inalámbrico", 8, 30],
    ["A003", "Teclado mecánico", 45, 40],
    ["A004", "Monitor 24\"", 12, 20],
    ["A005", "Impresora HP", 5, 10],
    ["A006", "Disco SSD 1TB", 25, 25]
]

def calcular_cantidad_pedido(stock_actual, stock_minimo):
    """Calcula cuántos artículos se deben pedir."""
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0

# (GENERAR PEDIDOS)

print("=== REPORTE DE PEDIDOS DE REABASTECIMIENTO ===\n")

pedidos = []

for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]
    
    cantidad_pedir = calcular_cantidad_pedido(stock_actual, stock_minimo)
    
    if cantidad_pedir > 0:
        pedidos.append((nombre, cantidad_pedir))
        print(f" {nombre}")
        print(f"   Cantidad a pedir: {cantidad_pedir} unidades")
        print(f"   Stock actual: {stock_actual} | Mínimo: {stock_minimo}")
        print("-" * 50)

if not pedidos:
    print(" No se necesitan pedidos. Todo el inventario está en niveles óptimos.")
else:
    print(f"\nTotal de artículos a pedir: {len(pedidos)}")