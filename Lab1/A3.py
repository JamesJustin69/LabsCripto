import os

# Asegurarse de que los colores ANSI funcionen en la terminal de Windows
if os.name == 'nt':
    os.system('color')

def descifrar_cesar(texto_cifrado):
    resultados = []

    for corrimiento in range(1, 26):
        resultado = ""
        for char in texto_cifrado:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                resultado += chr((ord(char) - base - corrimiento) % 26 + base)
            else:
                resultado += char
        resultados.append((corrimiento, resultado))

    return resultados

def resaltar_texto(texto):
    return f"\033[92m{texto}\033[0m"

def main():
    texto_cifrado = input("Introduce el texto cifrado: ")

    posibles_descifrados = descifrar_cesar(texto_cifrado)

    print("Posibles descifrados:")
    for corrimiento, texto in posibles_descifrados:
        if "seguridad en redes" in texto:  # Se destaca el texto más probable
            print(f"Corrimiento {corrimiento}: {resaltar_texto(texto)}")
        else:
            print(f"Corrimiento {corrimiento}: {texto}")

if __name__ == "__main__":
    main()
