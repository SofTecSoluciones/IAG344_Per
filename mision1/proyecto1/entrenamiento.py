# librerías
import re
"""
Espresiones regulares en Python
Problemas Reales 
"""
#Codigo
print("Librería cargada correctamente")
# Ejemplo1
texto="Mi Número es 12345"
resultado=re.search(r"\d+",texto)
print(f"{texto} Resultado {resultado.group()}")   
texto="Mi Número es 12345-985"
resultado=re.search(r"\d+",texto)
print(f"{texto} Resultado {resultado.group()}")   
texto="Mi Número es 123*45-985"
resultado=re.findall(r"\d+",texto)
print(f"{texto} Resultado {resultado}")

documento1="75,055,60"

def clean_id(documento):
  return re.sub(r"\D","",documento)
print(clean_id(documento1))
  