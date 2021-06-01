
import string

def divmod_excel(n):
    a, b = divmod(n, 26)
    if b == 0:
        return a - 1, b + 26
    return a, b

def alphabet_decode(value, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    value.isalpha()
    value = value.upper()[::-1]
    number = 0
    for i in range(len(value)):
        x = (len(alphabet) ** i)
        number = ( x * alphabet.index(value[i])) + number
    return number

def to_excel(num):
    chars = []
    while num > 0:
        num, d = divmod_excel(num)
        chars.append(string.ascii_uppercase[d])
    return ''.join(reversed(chars))

def validar_clave_segun_texto(texto, n):
    largo_texto = len(texto)
    while (26 ** largo_texto > n):
        print('Su N no permite resolver un texto de',largo_texto, 'caracteres, ingrese un N mayor')
        n=int(input("Ingresar N:"))
    return n


##Clave pública: (N, e)
##
##Clave privada (secreta): d
##
##Para cifrar un mensaje M, dando como resultado el mensaje cifrado C, se calcula:
##C = Me mod N

#La clave pública de B será entonces (nb,eb) = (46927,39423).


texto_plano=input("Ingresar Texto Cifrado:")
n=int(input("Ingresar Clave Privada (N):"))
e=int(input("Ingresar Clave Privada (D):"))

#n = validar_clave_segun_texto(texto_plano, n)
m = alphabet_decode(texto_plano)

result = 1
while e>0:
    if (e & 1) != 0:
        result = result * m
        result = result % n
    m = m*m
    m = m % n
    e = e>>1

#print('Utilizando clave privada ():',result)
print('Texto decodificado:',to_excel(result))