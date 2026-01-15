import re

texto = "Mi número es 12345"
resultado = re.search(r"\d+", texto) # busca 
print (resultado.group())
