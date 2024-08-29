def cifrar_cesar(texto, corrimiento):
    resultado = ""
    
    # Iterar a través de cada carácter en el texto
    for char in texto:
        # Verificar si el carácter es una letra
        if char.isalpha():
            # Determinar el rango del carácter (mayúscula o minúscula)
            base = ord('A') if char.isupper() else ord('a')
            # Aplicar el corrimiento, manteniendo el resultado dentro del rango de 'A' a 'Z' o 'a' a 'z'
            resultado += chr((ord(char) - base + corrimiento) % 26 + base)
        else:
            # Si el carácter no es una letra, añadirlo sin cambios
            resultado += char
    
    return resultado

# Ejemplo de uso
texto = input("Introduce el texto a cifrar: ")
corrimiento = int(input("Introduce el corrimiento: "))

texto_cifrado = cifrar_cesar(texto, corrimiento)
print("Texto cifrado:", texto_cifrado)
