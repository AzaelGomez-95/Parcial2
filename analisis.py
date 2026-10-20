import pandas as pd
import numpy as np

# Configurar semilla para reproducibilidad
np.random.seed(42)

# Datos base
sucursales = ['San Salvador', 'Santa Ana', 'San Miguel', 'La Libertad', 'Sonsonate']
categorias = ['Tecnología', 'Línea Blanca', 'Hogar', 'Ferreecaría', 'Electrodomésticos']
productos = [
    ('P001', 'Smart TV 55"', 'Tecnología'),
    ('P002', 'Refrigeradora 2 Puertas', 'Línea Blanca'),
    ('P003', 'Licuadora de Alta Potencia', 'Electrodomésticos'),
    ('P004', 'Taladro Percutor', 'Ferretería'),
    ('P005', 'Juego de Sala Minimalista', 'Hogar'),
    ('P006', 'Laptop Core i5', 'Tecnología'),
    ('P007', 'Microondas 20L', 'Electrodomésticos'),
    ('P008', 'Set de Herramientas 100 pzas', 'Ferretería'),
    ('P009', 'Aire Acondicionado 12000 BTU', 'Línea Blanca'),
    ('P010', 'Colchón Matrimonial Ortopédico', 'Hogar')
]

# Generar registros combinando productos y sucursales
data = []
for suc in sucursales:
    for prod in productos:
        stock = np.random.randint(5, 120)
        # Precio base con pequeña variación aleatoria según producto
        precio_base = {'Tecnología': 450.0, 'Línea Blanca': 380.0, 'Electrodomésticos': 65.0, 
                       'Ferretería': 85.0, 'Hogar': 250.0}[prod[2]]
        precio = round(precio_base * np.random.uniform(0.95, 1.05), 2)
        
        data.append({
            'id_producto': prod[0],
            'nombre_producto': prod[1],
            'categoria': prod[2],
            'sucursal': suc,
            'stock': stock,
            'precio_unitario': precio
        })

df_inventario = pd.DataFrame(data)
df_inventario.to_csv('inventario_sucursales.csv', index=False)
print("¡Dataset 'inventario_sucursales.csv' generado con éxito!")