#analizador de contraseña
import string
contraseña = input("Ingrese la contraseña: ")
longitud_correcta = len(contraseña) >= 8
contra_mayu = any(letra.isupper() for letra in contraseña)
contra_minu = any(letra.islower() for letra in contraseña)
contra_num = any(numero.isdigit() for numero in contraseña)
contra_sig = any(signos in string.punctuation for signos in contraseña)

print(f"caracteres correctos: {longitud_correcta}")
print(f"¿tiene mayusculas?: {contra_mayu}")
print(f"¿tiene minusculas?: {contra_minu}")
print(f"¿tiene numeros?: {contra_minu}")
print(f"¿tiene signos?: {contra_sig}")

#evaluar que nivel de seguridad tiene la contraseña
seguridad = sum([longitud_correcta, contra_mayu, contra_minu, contra_num, contra_sig])
if seguridad >= 2:
    print("nivel bajo de seguridad")
elif seguridad >=4:
    print("nivel medio de seguridad")
else:
    print("nivel alto de seguridad")