import pandas as pd
import numpy as np

# Estas 2 líneas hacen que pandas NO corte la visualización del DataFrame al imprimirlo
# sin ellas, si hay muchas columnas o filas pandas pone "..." en el medio
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# URL del dataset en GitHub
path = 'https://raw.githubusercontent.com/navnebror/ml_datasets/refs/heads/main/dirty_cafe_sales.json'

# ─────────────────────────────────────────────────────────────
# CARGA DEL DATASET
# pd.read_json() lee un archivo JSON y lo convierte directamente en un DataFrame.
# Un DataFrame es básicamente una tabla con filas y columnas, como Excel pero en Python.
# ─────────────────────────────────────────────────────────────
df = pd.read_json(path)

# df.head(30) devuelve los primeros 30 registros (filas) del DataFrame
datos = df.head(30)
print(datos)


# ─────────────────────────────────────────────────────────────
# 7. ELIMINAR FILAS CON None, NaN o null EN CUALQUIER COLUMNA
# ─────────────────────────────────────────────────────────────
# dropna() elimina TODAS las filas que tengan al menos un valor vacío/nulo en cualquier columna.
# None, NaN y null son distintas formas de representar "dato faltante" en Python/pandas.
# El resultado lo guardamos en un NUEVO DataFrame llamado df_clean (no modificamos el original df).
print('--7. Exclusión None, NaN, null--')
df_clean = df.dropna()

# .shape devuelve una tupla (filas, columnas) → nos dice cuántas filas quedaron después de limpiar
print(df_clean.shape)


# ─────────────────────────────────────────────────────────────
# 8. CORREGIR "Total Spent" DONDE NO COINCIDA CON Quantity * Price Per Unit
# ─────────────────────────────────────────────────────────────
print('--8. Total Spent Ajustado--')

# El problema: las columnas numéricas llegaron como strings ("2", "4.0", "ERROR").
# pd.to_numeric() intenta convertir cada valor a número.
# errors='coerce' significa: si un valor NO se puede convertir (ej: "ERROR", "UNKNOWN"),
# en lugar de lanzar un error, lo convierte en NaN.
df_clean['Quantity'] = pd.to_numeric(df_clean['Quantity'], errors='coerce')
df_clean['Price Per Unit'] = pd.to_numeric(df_clean['Price Per Unit'], errors='coerce')
df_clean['Total Spent'] = pd.to_numeric(df_clean['Total Spent'], errors='coerce')

# .info() muestra el tipo de dato de cada columna y cuántos valores no-nulos tiene.
# Sirve para confirmar que las 3 columnas ahora son float64 (número decimal) y no object (texto).
df_clean.info()

# df_clean.loc[condición, 'columna'] = valor  →  modifica SOLO las filas donde se cumple la condición.
# Condición: Total Spent != Quantity * Price Per Unit  (valores que NO coinciden)
# Para esas filas, sobreescribimos Total Spent con el cálculo correcto.
# Esto también corrige los NaN que quedaron de "ERROR"/"UNKNOWN" al convertir.
df_clean.loc[
    df_clean['Total Spent'] != df_clean['Quantity'] * df_clean['Price Per Unit'],
    'Total Spent'
] = df_clean['Quantity'] * df_clean['Price Per Unit']

# Mostramos los primeros 15 registros para verificar la corrección
print(df_clean.head(15))


# ─────────────────────────────────────────────────────────────
# 9. ELIMINAR FILAS QUE CONTENGAN "UNKNOWN" O "ERROR" EN CUALQUIER COLUMNA
# ─────────────────────────────────────────────────────────────
# Estrategia: usamos apply() para recorrer CADA celda del DataFrame y verificar
# si contiene exactamente "UNKNOWN" o "ERROR" (como string).
# ~  = NOT (negación lógica)
# .any(axis=1) = "al menos UNA columna de esa fila cumple la condición"
# Con el ~ al inicio, nos quedamos con las filas donde NINGUNA columna tiene esos valores.

print('--9. Exclusión UNKNOWN y ERROR--')

# Primero, para cada celda verificamos si es string y si es "UNKNOWN" o "ERROR"
mask_bad = df_clean.apply(
    lambda col: col.astype(str).isin(['UNKNOWN', 'ERROR'])
).any(axis=1)

# Nos quedamos con las filas donde mask_bad es False (no tienen valores malos)
df_clean = df_clean[~mask_bad]
print(df_clean.shape)


# ─────────────────────────────────────────────────────────────
# 10. ELIMINAR REGISTROS DUPLICADOS
# ─────────────────────────────────────────────────────────────
# drop_duplicates() elimina filas que sean exactamente iguales en TODAS las columnas.
# Por defecto conserva la PRIMERA aparición y elimina las repetidas.

print('--10. Eliminación de duplicados--')
df_clean = df_clean.drop_duplicates()
print(df_clean.shape)


# ─────────────────────────────────────────────────────────────
# 11. ESTANDARIZAR COLUMNAS DE TEXTO A MAYÚSCULAS
# ─────────────────────────────────────────────────────────────
# Problema: la misma categoría puede aparecer como "coffee", "Coffee", "COFFEE" → son distintas para pandas.
# Solución: convertir todo a MAYÚSCULAS para uniformizar.
#
# apply(lambda x: x.str.upper()) recorre cada columna especificada y convierte
# cada string a mayúsculas con .str.upper()

print('--11. Estandarización a mayúsculas--')
cols_texto = ['Item', 'Payment Method', 'Location']
df_clean[cols_texto] = df_clean[cols_texto].apply(lambda x: x.str.upper())
print(df_clean.head(10))


# ─────────────────────────────────────────────────────────────
# 12. CAMBIAR EL ÍNDICE DEL DATAFRAME AL "Transaction ID"
# ─────────────────────────────────────────────────────────────
# Por defecto pandas usa un índice numérico (0, 1, 2, 3...).
# set_index() cambia ese índice por la columna que le indiquemos.
# Así cada fila se identifica por su ID de transacción (TXN_XXXXXXX) en lugar de un número.

print('--12. Índice = Transaction ID--')
df_clean = df_clean.set_index('Transaction ID')
print(df_clean.head(5))


# ─────────────────────────────────────────────────────────────
# 13. ORDENAR EL DATAFRAME POR ÍNDICE DE FORMA ASCENDENTE
# ─────────────────────────────────────────────────────────────
# sort_index() ordena las filas según el valor del índice (Transaction ID).
# ascending=True  →  orden de menor a mayor (A→Z para strings, 0→N para números)

print('--13. Ordenado por Transaction ID ascendente--')
df_clean = df_clean.sort_index(ascending=True)
print(df_clean.head(10))


# ─────────────────────────────────────────────────────────────
# 14. MOSTRAR LOS PRIMEROS 30 REGISTROS EN UNA SOLA LÍNEA SIN print()
# ─────────────────────────────────────────────────────────────
# En Jupyter Notebook, escribir una expresión en la última línea de una celda
# la muestra automáticamente SIN necesidad de usar print().
# En un script .py normal esto no se ve, pero en Jupyter es la forma estándar.

df_clean.head(30)