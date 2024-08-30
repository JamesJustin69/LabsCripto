from scapy.all import *
import struct
import random
import time

def cifrar_cesar(texto, corrimiento):
    resultado = ""
    
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + corrimiento) % 26 + base)
        else:
            resultado += char
    
    return resultado

def enviar_paquete_icmp(destino, payload, id_icmp, seq_num):
    # Crear un paquete ICMP Echo Request
    paquete = IP(dst=destino) / ICMP(id=id_icmp, seq=seq_num) / Raw(load=payload)
    
    # Enviar el paquete
    send(paquete)

def main():
    # Solicitar el texto y el corrimiento del usuario
    texto = input("Introduce el texto a cifrar: ")
    corrimiento = int(input("Introduce el corrimiento: "))
    
    # Cifrar el texto
    texto_cifrado = cifrar_cesar(texto, corrimiento)
    destino = "8.8.8.8"  # Dirección IP de destino, puedes cambiarla según tus necesidades

    print("Texto cifrado:", texto_cifrado)

    # Filtrar espacios del texto cifrado
    texto_cifrado = texto_cifrado.replace(' ', '')

    # ID y secuencia para ICMP
    id_icmp = random.randint(0, 65535)  # ID aleatorio para simular tráfico real
    seq_num = 1

    for char in texto_cifrado:
        # Timestamp y Payload ICMP coherente
        timestamp = int(time.time())
        payload = struct.pack("!d", timestamp) + char.encode('utf-8') + b'\x00' * (64 - len(char) - struct.calcsize("!d"))

        print(f"Enviando carácter '{char}' en paquete ICMP...")
        enviar_paquete_icmp(destino, payload, id_icmp, seq_num)

        # Incrementar el número de secuencia para el siguiente paquete
        seq_num += 1
        time.sleep(1)  # Pausa para simular tráfico normal

    print("Todos los paquetes ICMP enviados.")

if __name__ == "__main__":
    main()
