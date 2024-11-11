from Crypto.Cipher import DES, AES, DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

#ajuste de clave
def ajustarTamClave(clave, tamBytes):
    if len(clave) < tamBytes:
        clave += get_random_bytes(tamBytes - len(clave))
    elif len(clave) > tamBytes:
        clave = clave[:tamBytes]

    print(f"clave ajustada: {clave.hex()}")

    return clave


#ciffrados

#DES DES.MODE_CBC
def cifDES(msj, clave, iv):
    c = DES.new(clave, DES.MODE_CBC, iv)
    msjCifrado = c.encrypt(pad(msj.encode(), DES.block_size))

    return base64.b64encode(msjCifrado).decode()

def desDES(msjCifrado, clave, iv):
    msjCifrado = base64.b64decode(msjCifrado)
    d = DES.new(clave, DES.MODE_CBC, iv)
    msjDescifrado = unpad(d.decrypt(msjCifrado), DES.block_size)

    return msjDescifrado.decode()

#AEeS-256 xd
def cifAES(msj, clave, iv):
    c = AES.new(clave, AES.MODE_CBC, iv)
    msjCifrado = c.encrypt(pad(msj.encode(), AES.block_size))

    return base64.b64encode(msjCifrado).decode()

def desAES(msjCifrado, clave, iv):
    msjCifrado = base64.b64decode(msjCifrado)
    d = AES.new(clave, AES.MODE_CBC, iv)
    msjDescifrado = unpad(d.decrypt(msjCifrado), AES.block_size)

    return msjDescifrado.decode()

#3dES
def cif3DES(msj, clave, iv):
    c = DES3.new(clave, DES3.MODE_CBC, iv)
    msjCifrado = c.encrypt(pad(msj.encode(), DES3.block_size))

    return base64.b64encode(msjCifrado).decode()

def des3DES(msjCifrado, clave, iv):
    msjCifrado = base64.b64decode(msjCifrado)
    d = DES3.new(clave, DES3.MODE_CBC, iv)
    msjDescifrado = unpad(d.decrypt(msjCifrado), DES3.block_size)

    return msjDescifrado.decode()

#resto

algs = {'DES': (DES, 8), 'AES-256': (AES, 32), '3DES': (DES3, 24)}

for nombre, (algoritmo, tamBytes) in algs.items():
    print(f"\n {nombre} ")
    clave = input(f"Ingresar clave para el algoritmo {nombre}: ").encode()
    iv = input(f"Ingresar IV correcto (8 bytes - DES y 3DES; 16 bytes - AES) para el algoritmo {nombre}: ").encode()
    msj = input(f"Ingresar mensaje para cifrar con el algoritmo {nombre}: ")

    claveTamCorrecto = ajustarTamClave(clave, tamBytes)

    if nombre == 'DES':
        msjC = cifDES(msj, claveTamCorrecto, iv)
        msjD = desDES(msjC, claveTamCorrecto, iv)
    elif nombre == 'AES-256':
        msjC = cifAES(msj, claveTamCorrecto, iv)
        msjD = desAES(msjC, claveTamCorrecto, iv)
    elif nombre == '3DES':
        msjC = cif3DES(msj, claveTamCorrecto, iv)
        msjD = des3DES(msjC, claveTamCorrecto, iv)

    print(f"Mensaje OG: {msjC}")
    print(f"Mensaje Descifrado: {msjD}")
