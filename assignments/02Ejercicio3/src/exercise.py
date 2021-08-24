def opAritmetica(a, b, clave):
    if clave == 's':
        return a + b
    elif clave == 'r':
        return a - b
    elif clave == 'm':
        return a * b
    elif clave == 'd':
        return a / b
    else:
        return "clave invalida"

def main():
    n1 = int(input("Dame el valor de un primer numero:"))
    n2 = int(input("Dame el valor de un segundo numero:"))
    respuesta = input("Dame la clave (s=suma/r=resta/m=multiplicacion/d=division) ?")

    resultado=opAritmetica(n1, n2, respuesta)

    print(resultado)

if __name__=='__main__':
    main()
