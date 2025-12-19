#pedir al usuario un texto
texto = input("ingrese el texto: ").lower()
texto_limpio = texto.strip()
print(f"texto original: {texto}")
print(f"texto en mayusculas: {texto_limpio.upper()}")
print(f"texto en minusculas: {texto_limpio.lower()}")
palabra = texto_limpio.split()
cantidad_p = len(palabra)
print(f"la cantidad de palabras que tiene son: {cantidad_p}")
print(f"primera letra: {texto_limpio[0]}")
print(f"ultima letra: {texto_limpio[-1]}")
vocal = texto[0].lower()
empieza_v = vocal in "aeiou "
print(f"empieza por vocal?: {empieza_v}")
constante = texto[-1].lower()
termina_c = constante not in "aeiou"
print(f"¿termina en constante?: {termina_c}")
print(f"texto invertido: {texto_limpio[::-1]}")
vocales_r = "aeiou"
for a in vocales_r:
    texto_limpio = texto_limpio.replace(a, "*")
print(f"texto remplazado las vocales: {texto_limpio}")