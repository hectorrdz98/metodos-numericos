import math

def convertirBinario(numEntero):
    return int(bin(numEntero)[2:])

def convertirDecimal(numBinario):
    return int(str(numBinario), 2)

def convertirFraccionBinario(numFraccion, cifras):
    res = ''
    while numFraccion > 0 and cifras > 0:
        numFraccion *= 2
        res += str(str(numFraccion).split(".")[0])
        numFraccion = float('.' + str(numFraccion).split(".")[1])
        cifras -= 1
    return res

def convertirFraccionDecimal(numFraccion, cifras):
    return 0

if input("Binario a Decimal (bd) o Decimal a Binario (db)? ") == 'db':
    num = input("Ingresa el numero decimal a volver binario: ")
    entero = num.split(".")[0]
    parteEntera = convertirBinario(int(entero))
    res = str(parteEntera)
    if len(num.split(".")) > 1:
        decimal = '0.' + num.split(".")[1]
        res += '.' + convertirFraccionBinario(float(decimal), 5)
    print("El binario es:", res)

else:
    num = input("Ingresa el numero binario a volver decimal: ")
    entero = num.split(".")[0]
    parteEntera = convertirDecimal(int(entero))
    res = str(parteEntera)
    """if len(num.split(".")) > 1:
        decimal = num.split(".")[1]
        res += '.' + str(convertirFraccionDecimal(float('.'+decimal), 5))
    """
    print("El numero decimal es:", res)