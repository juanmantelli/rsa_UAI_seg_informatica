import random

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es número primo")
            return False
    print("Número primo verificado")
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Algoritmo extendido euclidiano para encontrar el inverso multiplicativo de dos números
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2- temp1* x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

def genera_par_claves(p, q):
    n = p * q

    #Phi ø
    phi = (p-1) * (q-1)

    #Un número entero e tal que e y phi (n) son coprimos
    e = random.randrange(1, phi)

    #Algoritmo de Euclides para verificar que e y phi (n) son coprimo
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #Algoritmo extendido de Euclid para generar la clave privada
    d = multiplicative_inverse(e, phi)

    #La clave publica es (e, n) y la clave privada es (d, n)
    return ((e, n), (d, n))


if __name__ == '__main__':
    
    p=int(input("Numero primo P:"))
    while not es_primo(p):
        p=int(input("Numero primo P:"))

    q=int(input("Numero primo Q:"))
    while not es_primo(q):
        q=int(input("Numero primo Q:"))

    public, private = genera_par_claves(p, q)
    print("KU:", public ," y KR:", private)